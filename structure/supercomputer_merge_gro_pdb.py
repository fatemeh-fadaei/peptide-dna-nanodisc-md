#!/usr/bin/env python3

#python merge_gro_pdb.py -dna DNA.gro -dmpc DMPC_reduce_reordered.pdb -o DNA_DMPC_merged.gro

import argparse
import MDAnalysis as mda

ap = argparse.ArgumentParser(description="Merge DNA (.gro) and DMPC (.pdb) into one .gro")
ap.add_argument("-dna", required=True, help="DNA.gro file")
ap.add_argument("-dmpc", required=True, help="DMPC.gro file")
ap.add_argument("-o", "--out", required=True, help="Output merged .gro file")
args = ap.parse_args()

# Load structures
u_dna  = mda.Universe(args.dna)
u_dmpc = mda.Universe(args.dmpc)
u_dmpc_only_DMPC=u_dmpc.select_atoms("resname DMPC")

# Merge in order: DNA first, then DMPC
merged = mda.Merge(u_dna.atoms, u_dmpc_only_DMPC.atoms)

# Write GRO
merged.atoms.write(args.out)
print(f"[DONE] Wrote merged GRO: {args.out}")
