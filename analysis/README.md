# Analysis Scripts

This folder contains scripts for analyzing molecular dynamics (MD) simulations of peptide–DNA nanodiscs, with a focus on lipid–protein interactions.

* [analysis_protein_residue_to_dmpc_tail_distance.sh](analysis_protein_residue_to_dmpc_tail_distance.sh)  
  Computes the minimum distance between protein residues and DMPC lipid tail atoms using GROMACS `gmx pairdist`.
  
* [phe_residue_dmpc_distance_time.sh](phe_residue_dmpc_distance_time.sh)  
  Calculates time-dependent distances between PHE residues and DMPC lipid tails using `gmx pairdist`.

* [chain_tilt_angle_vs_z.sh](chain_tilt_angle_vs_z.sh)  
  Calculates tilt angles of peptide chains relative to the z-axis using `gmx gangle`.
