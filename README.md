# dna_nanodisc_pep
Script used to set up the system
## check_DNA_seq.ipynb

This notebook is used to verify the DNA sequence used in the nanodisc system.  
It checks the full sequence, identifies repeated motifs, and confirms the correct arrangement of the 21-bp units that form the circular DNA scaffold.

### What this script does
- Loads the DNA sequence used for building the nanodisc.
- Detects repeated sequence units within the 147-bp circular DNA.
- Identifies the start and end positions of each repeat.
- Ensures that the pattern is consistent across the entire sequence.
- Helps validate the input DNA before running MD simulations.

### Why this script is useful
DNA nanodisc construction requires a perfectly repeated 21-bp motif.  
This notebook ensures that the sequence is correct, error-free, and suitable for downstream molecular dynamics simulations.

### How to use
1. Open the notebook in Jupyter or VS Code.
2. Run all cells.
3. Review the printed positions of each repeated sequence.
4. Confirm that the expected seven 21-bp repeats are present.

### Output
The script prints:
- the detected pattern  
- the number of repeats  
- the start and end positions of each repeat  
This allows quick validation of the nanodisc DNA sequence.
