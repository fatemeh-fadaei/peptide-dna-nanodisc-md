# dna_nanodisc_pep
Script used to set up the system

## check_DNA_seq.ipynb
Verify the DNA sequence used in the nanodisc. It detects the repeated 21-bp motif, checks all repeat positions, and confirms that the full 147-bp sequence is correct.

### 2_script_final_remove_clashes
Remove atomic clashes from the initial nanodisc structure.

### 3_script_check_dmpc_ring_piercing
Check if any DMPC lipids pierce through the peptide ring.

### 4_find_bp_distance_restrain.ipynb
Compute base-pair distances and prepare distance-based restraints.

### 4_script_define_BB_SC
Generate backbone and side-chain selections for analysis.

### 6_Average Protein–DMPC Distance per Residue
Calculate the average distance between each peptide residue and DMPC lipids.

### merge_gro_pdb.py
Merge `.gro` and `.pdb` files to create a combined coordinate file.

### reorder_dmpc_by_itp.py
Reorder DMPC atoms to match the `.itp` file specification.

### script_pymol_verify_no_dmpc_near_ring.txt
PyMOL script to verify that no DMPC lipids remain near the peptide ring.
