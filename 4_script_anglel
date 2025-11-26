#!/bin/bash

GMX="/home/fatemeh/anaconda3/envs/gromacs_2024_4/bin.AVX2_256/gmx"
TPR="nanodisc_pos_381dmpc_100ns-200ns.tpr"
XTC="nanodisc_pos_381dmpc_total_200ns_correct.xtc"



# Define all chain pairs
chains=(
  "2 20"
  "41 59"
  "61 79"
  "100 118"
  "120 138"
  "159 177"
  "179 197"
  "218 236"
  "238 256"
  "277 295"
  "297 315"
  "336 354"
  "356 374"
  "395 413"
)

# Create all index groups in one file
echo "Creating index groups..."
for i in "${!chains[@]}"; do
  pair=(${chains[$i]})
  res1=${pair[0]}
  res2=${pair[1]}
  chain_num=$((i + 1))
  
  gmx select -s "$TPR" \
    -select "\"chain${chain_num}\" name CA and (resnr ${res1} or resnr ${res2})" \
    -on chain${chain_num}.ndx
done

# Calculate tilt angles for each chain
echo "Calculating tilt angles..."
for i in "${!chains[@]}"; do
  chain_num=$((i + 1))
  
  echo "Processing chain ${chain_num}..."
  gmx gangle -s "$TPR" -f "$XTC" -n chain${chain_num}.ndx \
    -g1 vector -group1 chain${chain_num} -g2 z \
    -oav chain${chain_num}_tilt_vsZ.xvg -oh chain${chain_num}_tilt_hist.xvg
done

echo "Done! Output files: chain*_tilt_vsZ.xvg and chain*_tilt_hist.xvg"
