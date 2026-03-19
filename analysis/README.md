# Analysis Scripts

This folder contains scripts for analyzing molecular dynamics (MD) simulations of peptide–DNA nanodiscs, with a focus on lipid–protein interactions.

* [analysis_protein_residue_to_dmpc_tail_distance.sh](analysis_protein_residue_to_dmpc_tail_distance.sh)  
  Computes the minimum distance between protein residues and DMPC lipid tail atoms using GROMACS `gmx pairdist`.
  
* [phe_residue_dmpc_distance_time.sh](phe_residue_dmpc_distance_time.sh)  
  Calculates time-dependent distances between PHE residues and DMPC lipid tails using `gmx pairdist`.

* [chain_tilt_angle_vs_z.sh](chain_tilt_angle_vs_z.sh)  
  Calculates tilt angles of peptide chains relative to the z-axis using `gmx gangle`.

* [residue_dmpc_distance_plot.py](residue_dmpc_distance_plot.py)
  Computes and plots average protein–DMPC distances per residue across multiple chains.

* [plot_tilt_angle_time_comparison.ipynb](plot_tilt_angle_time_comparison.ipynb)  
  Plots the smoothed average tilt angle vs time for multiple chains and compares systems.

* [pymol_verify_no_dmpc_near_ring.py](pymol_verify_no_dmpc_near_ring.py)
  PyMOL script to detect and visualize DMPC lipids within 2.2 Å of aromatic residues (PHE, TYR, TRP).

* [pymol_dna_nanodisc_neg4f_visualization.ipynb](pymol_dna_nanodisc_neg4f_visualization.ipynb)
  PyMOL visualization of DNA–lipid nanodisc with peptide(neg4f) conjugates
