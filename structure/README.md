# Structure Preparation

Scripts used to build and prepare the peptide–DNA nanodisc system for molecular dynamics simulations.


  
* [merge_center_clean_minimize_nanodisc.sh](merge_center_clean_minimize_nanodisc.sh)
  Builds the nanodisc system by merging DNA and lipid bilayer, removing lipid clashes, centering the system, and performing energy minimization.
  
* [check_dmpc_ring_piercing.sh](check_dmpc_ring_piercing.sh)  
  Removes DMPC lipids that penetrate aromatic ring regions and generates a cleaned structure with reduced lipid–protein clashes.

* [build_bp_distance_restraints.ipynb](build_bp_distance_restraints.ipynb)  
  Generates base-pair distance restraints and writes them into GROMACS topology format.

* [define_backbone_sidechain_groups.sh](define_backbone_sidechain_groups.sh) 
  Creates backbone and side-chain groups and generates position restraint files for MD simulations.
  
* [estimate_lipid_count_from_diameter.ipynb](estimate_lipid_count_from_diameter.ipynb) 
  Estimates the number of lipids in a nanodisc from its diameter using geometric calculations.
