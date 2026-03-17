# Structure Preparation

Scripts used to build and prepare the peptide–DNA nanodisc system for molecular dynamics simulations.


  
* [merge_center_clean_minimize_nanodisc.sh](merge_center_clean_minimize_nanodisc.sh)
  Builds the nanodisc system by merging DNA and lipid bilayer, removing lipid clashes, centering the system, and performing energy minimization.
  
  *[check_dmpc_ring_piercing.sh](check_dmpc_ring_piercing.sh)  
  Removes DMPC lipids that penetrate aromatic ring regions and generates a cleaned structure with reduced lipid–protein clashes.
