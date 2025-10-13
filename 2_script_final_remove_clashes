merged_TOP=
merged=nanodisc_bilayer_310K
mini=minimization_mdp/minim3.mdp                   #fix all atoms of dna and peptides 
mini2=minimization_mdp/minim5-02.mdp                 #no restraint
clean_top=nanodisc_bilayer_310K.top
################################################
#
#################################################
### Step 1: Center the system at (0, 0, 0)
#gmx editconf -f "${merged}" -o "${merged}_box_center.gro"  -center 0 0 0 -box 21 21 12
#gmx make_ndx -f "${merged}_box_center.gro"  -o "${merged}_box_center.ndx"<<EOF
#1 & r PHE & a CG CD1 CD2 CE1 CE2 CZ
#1& r TYR & a CG CD1 CD2 CE1 CE2 CZ
#1& r TRP & a CG CD1 CD2 NE1 CE2 CE3 CZ2 CZ3 CH2
#q
#EOF
##
##################################################
####remove clashes
###################################################
#close=0.05
## Step 2: Generate index file excluding unwanted DMPC
#gmx select -f "${merged}_box_center.gro" \
#           -s "${merged}_box_center.gro" \
#           -n "${merged}_box_center.ndx"\
#           -on "keep${close}.ndx" \
#             -select 'group "System" and not (resname DMPC and same residue as ((distance from [0, 0, 0] > 7) or (within 0.05 of (group "Protein" and not name "H*"))))'
### Step 3: Write cleaned structure
#
#gmx editconf -f "${merged}_box_center.gro" -n "keep${close}.ndx" -o "${merged}_box_center_clean.gro"
## Step 4: Count DMPC residues before and after
#awk 'substr($0,6,4)=="DMPC"{r[substr($0,1,5)]++} END{print "Before:",length(r)}' "${merged}_box_center.gro"
#awk 'substr($0,6,4)=="DMPC"{r[substr($0,1,5)]++} END{print "After :",length(r)}' "${merged}_box_center_clean.gro"
###################################################################################
#gmx editconf -f "${merged}_box_center_clean.gro" -bt cubic -c -d 1.2 -o "${merged}_box_center_clean_box.gro"
gmx grompp -f  $mini -p  $clean_top -c "${merged}_box_center_clean_box.gro" -r "${merged}_box_center_clean_box.gro" -o "${merged}_box_center_clean_box_min1.tpr" -maxwarn 1 
gmx_d mdrun -v -deffnm "${merged}_box_center_clean_box_min1"
#gmx grompp -f $mini2 -p $clean_top -c "${merged}_box_center_clean_box_min1.gro" -o "${merged}_box_center_clean_box_min1_min2.tpr"  -maxwarn 1 
#gmx_d mdrun -v -deffnm "${merged}_box_center_clean_box_min1_min2"  
######################################################################################












