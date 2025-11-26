#!/bin/bash
# ========= USER INPUTS =========
# ========= USER INPUTS =========
GMX="/home/fatemeh/anaconda3/envs/gromacs_2024_4/bin.AVX2_256/gmx"
TPR="nanodisc_pos_381dmpc_100ns-200ns.tpr"
TRAJ="nanodisc_pos_381dmpc_total_200ns_correct.xtc"
NDX="nanodisc_pos_381_analysis.ndx"
OUT_PREFIX="Positive_PHE_residue_dmpc_distance.xvg"


# ========= STEP 1: CREATE INDEX FILE =========
#echo "🧩 Creating residue + DMPC tail index file..."


#$GMX make_ndx -f "$TPR"   -n "$NDX"  -o "$NDX"<<EOF
#1& r PHE 
#24 &! a H* N CA C O
#q
#EOF
$GMX make_ndx -f "$TPR" -o "$NDX" -n "$NDX"





$GMX pairdist \
    -f "$TRAJ" \
    -s "$TPR" \
    -n "$NDX" \
    -sel  'group "Protein_&_PHE_&_!H*_N_CA_C_O"' \
    -ref 'group "DMPC_&_C22_C23_C24_C25_C26_C27_C28_C29_C210_C211_C212_C213_C214_C314_C313_C312_C311_C310_C39_C38_C37_C36_C35_C34_C33_C32"' \
    -selgrouping all \
    -refgrouping all \
    -seltype res_com\
    -selrpos atom \
    -cutoff 2\
    -tu ns\
    -o $OUT_PREFIX








