#!/usr/bin/env python3


#python reorder_dmpc_by_itp.py   --pdb system.pdb --itp /fs/ess/PGS0330/fatemeh/nanodiscs_peptides/negative/neg02/topologies/DMPC.itp  -o system_reordered.pdb --renumber



import argparse, re
import MDAnalysis as mda
from MDAnalysis.coordinates.PDB import PDBWriter
from collections import defaultdict, Counter

def parse_itp_atoms(itp_path):
    """Return the ordered list of atom names from [ atoms ] in a GROMACS .itp."""
    order, in_atoms = [], False
    with open(itp_path, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith(';'):
                continue
            if s.startswith('['):
                in_atoms = s.lower().startswith('[ atoms')
                continue
            if in_atoms:
                s = s.split(';', 1)[0].strip()
                if not s:
                    continue
                cols = re.split(r'\s+', s)
                if len(cols) >= 5:
                    order.append(cols[4])  # column 5 is atom name
    if not order:
        raise ValueError(f"No atom names parsed from [ atoms ] in {itp_path}")
    return order

def reorder_single_residue(residue, desired_order):
    """Reorder atoms inside one residue by exact atom-name match."""
    name2atoms = defaultdict(list)
    for a in residue.atoms:
        name2atoms[a.name.strip()].append(a)

    ordered_atoms, missing = [], []
    for name in desired_order:
        name = name.strip()
        if name2atoms[name]:
            ordered_atoms.append(name2atoms[name].pop(0))
        else:
            missing.append(name)

    extras = []
    for k, lst in name2atoms.items():
        if lst:
            extras.extend([k] * len(lst))

    # Keep unmatched leftovers at the end to avoid atom loss
    for k, lst in name2atoms.items():
        ordered_atoms.extend(lst)

    return ordered_atoms, missing, extras

def main():
    ap = argparse.ArgumentParser(description="Reorder ONLY DMPC residues in a PDB to match dmpc.itp [ atoms ] order.")
    ap.add_argument("--pdb", required=True, help="Input PDB")
    ap.add_argument("--itp", required=True, help="DMPC .itp with [ atoms ]")
    ap.add_argument("-o", "--out", required=True, help="Output PDB")
    ap.add_argument("--renumber", action="store_true", help="Renumber atom serials 1..N in output")
    ap.add_argument("--report", default="reorder_report.tsv", help="Report TSV of any mismatches")
    args = ap.parse_args()

    desired = parse_itp_atoms(args.itp)
    u = mda.Universe(args.pdb)

    new_atoms = []
    touched, total_dmpc = 0, 0
    issues = []

    for res in u.residues:
        if res.resname.strip() == "DMPC":
            total_dmpc += 1
            atoms, missing, extras = reorder_single_residue(res, desired)
            new_atoms.extend(atoms)
            touched += 1
            if missing or extras:
                issues.append((res.segid, res.resid, Counter(missing), Counter(extras)))
        else:
            new_atoms.extend(list(res.atoms))

    new_u = mda.Merge(mda.AtomGroup(new_atoms))

    if args.renumber:
        for i, a in enumerate(new_u.atoms, start=1):
            a.id = i

    with PDBWriter(args.out, multiframe=False) as w:
        w.write(new_u)

    # Report
    with open(args.report, "w", encoding="utf-8") as f:
        f.write("segid\tresid\tmissing_atom_names\textra_atom_names\n")
        for segid, resid, miss, extra in issues:
            miss_str = ",".join([f"{k}x{v}" for k, v in miss.items()]) if miss else "-"
            extra_str = ",".join([f"{k}x{v}" for k, v in extra.items()]) if extra else "-"
            f.write(f"{segid}\t{resid}\t{miss_str}\t{extra_str}\n")

    print(f"[DONE] Wrote: {args.out}")
    print(f"[INFO] DMPC residues: {total_dmpc}, reordered: {touched}")
    if issues:
        print(f"[WARN] Some mismatches found. See {args.report}")

if __name__ == "__main__":
    main()
