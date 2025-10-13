GRO=final_nanodisc_bilayer_310K_final_clean_min
m

#
#
#################################################
#
gmx make_ndx -f "$GRO.gro" -o "GRO.ndx"<<EOF
1 & a N CA C 
1 & a P O2P O1P O5' O3' C5' C4' C3' O4' C2' C1'
1  & ! a H*  N CA C P O2P O1P O5' O3' C5' C4' C3' O4' C2' C1'
q
EOF
gmx make_ndx -f "$GRO.gro" -n "GRO.ndx" -o "GRO.ndx" 
#29 sidechain-H         :  4606 atoms
#30 backbone_DNA_Protein:  4039 atoms
gmx editconf -f "$GRO.gro" -n "GRO.ndx" -o "check_restrain_sidechain.gro"
gmx editconf -f "$GRO.gro" -n "GRO.ndx" -o "check_restrain_backbone.gro" 
gmx genrestr -f "$GRO.gro" -n "GRO.ndx" -o "restrain_sidechain_DNA_PEP.itp"
gmx genrestr -f "$GRO.gro" -n "GRO.ndx" -o "restrain_backbone_DNA_PEP.itp"





