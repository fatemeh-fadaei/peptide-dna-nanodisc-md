#!/bin/bash
# ========= USER INPUTS =========
GMX="/home/fatemeh/anaconda3/envs/gromacs_2024_4/bin.AVX2_256/gmx"
TPR="nanodisc_pos_381dmpc_100ns-200ns.tpr"
TRAJ="nanodisc_pos_381dmpc_total_200ns_correct.xtc"
NDX="nanodisc_pos_381_analysis.ndx"
OUT_PREFIX="pos_residue_dmpc_distance"

# ========= STEP 1: CREATE INDEX FILE =========
#echo "🧩 Creating residue + DMPC tail index file..."


$GMX make_ndx -f "$TPR" -o "$NDX"<<EOF
13 & a C22  C23 C24  C25 C26  C27  C28  C29  C210 C211 C212 C213 C214 C314  C313 C312  C311  C310  C39  C38  C37 C36 C35 C34 C33  C32
1 & !r DA DC DG DT TO3 TO5  
22 &! a H* N CA C O 
q
EOF

$GMX make_ndx -f "$TPR" -o "$NDX" -n "$NDX"
#$GMX editconf -f "$TPR" -n "$NDX" -o "check_ndx_alkylchain.pdb"

$GMX pairdist \
    -f "$TRAJ" \
    -s "$TPR" \
    -n "$NDX" \
    -sel  'group "Protein_&_!DA_DC_DG_DT_TO3_TO5_&_!H*_N_CA_C_O"' \
    -ref 'group "DMPC_&_C22_C23_C24_C25_C26_C27_C28_C29_C210_C211_C212_C213_C214_C314_C313_C312_C311_C310_C39_C38_C37_C36_C35_C34_C33_C32"' \
    -selgrouping res \
    -refgrouping all \
    -seltype res_com\
    -selrpos atom \
    -cutoff 2\
    -tu ns\
    -o "${OUT_PREFIX}_final.xvg" 


$GMX editconf -f "$TPR" -n "$NDX" -o "check_ndx_alkylchain.pdb"
$GMX editconf -f "$TPR" -n "$NDX" -o "check_ndx_sidechain.pdb"




