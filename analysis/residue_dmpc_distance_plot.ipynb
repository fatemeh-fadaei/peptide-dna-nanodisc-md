import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === 1️⃣ Load and clean the XVG file ===
filename = "residue_dmpc_distance_final.xvg"

with open(filename) as f:
    lines = [line for line in f if not line.startswith(('#', '@')) and line.strip()]

# Convert each line to list of floats
data_lines = [[float(x) for x in line.split()] for line in lines]
df = pd.DataFrame(data_lines)
print("DataFrame shape:", df.shape)   # for debugging
print(df.head())                      # for debugging
# First column = time; rest = distances
time = df.iloc[:, 0]
distances = df.iloc[:, 1:]
#distances.to_csv("distances_debug.csv")  # for debugging




# === 2️⃣ Compute mean distance for each residue ===
mean_dist = distances.mean()              #averages each column (over all time frames).
mean_dist = mean_dist.reset_index(drop=True)
print("Mean distances shape:", mean_dist.shape)  # for debugging
print("averages each column (over all time frames):\n", mean_dist.head())                       # for debugging




# === 3️⃣ Define chain ranges (each with 19 residues) ===
chain_ranges = [
    (1, 19), (20, 38), (39, 57), (58, 76), (77, 95), (96, 114),
    (115, 133), (134, 152), (153, 171), (172, 190),
    (191, 209), (210, 228), (229, 247), (248, 266)
]

res_per_chain = 19  # since each chain has 19 residues

avg_per_position = []
std_per_position = []

for pos in range(res_per_chain):  # This loop runs 19 times, once for each residue position (1 to 19).
    # Get indices of the same residue position in all 14 chains
    #start → fixed for each chain (it tells where that chain begins).
    #pos → changes every time the loop runs (it moves through residues 1 → 19).
    idxs = []
    for (start, end) in chain_ranges:      #This loop goes through every chain (14 chains total)
        idxs.append((start - 1) + pos)
    
    # Calculate mean and std for that residue position
    avg = mean_dist.iloc[idxs].mean()
    std = mean_dist.iloc[idxs].std()
    
    avg_per_position.append(avg)
    std_per_position.append(std)
print("Average per position:", avg_per_position)  # for debugging

# === 5️⃣ Residue names from your sequence ===
labels = ["ASP", "TRP", "PHE", "GLN", "ALA", "PHE", "TYR", "ASP", "GLN",
          "VAL", "ALA", "GLU", "GLN", "PHE", "GLN", "GLU", "ALA", "PHE", "GLY"]


# === 1️⃣ Define color mapping ===


colors = []
for res in labels:
    if res == "PHE":
        colors.append("green")
    elif res == "GLN":
        colors.append("orange")
    elif res == "ARG":
        colors.append("#FF69B4")
    elif res == "TYR":
        colors.append("red")
    else:
        colors.append("gray")




fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(labels))

bars = ax.bar(
    x, avg_per_position, color=colors, edgecolor="black", linewidth=1
)

# ✅ Correct: set the y-axis limit
ax.set_ylim(0, 2)

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, fontsize=10)
ax.set_xlabel("Residue (Position in Sequence)", fontsize=12)
ax.set_ylabel("Average Distance to DMPC (nm)", fontsize=12)
ax.set_title("Average Protein–DMPC Distance per Residue (Averaged Across 14 Chains)", fontsize=13)

# # Add numeric labels above bars
# for bar, val in zip(bars, avg_per_position):
#     ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
#             f"{val:.2f}", ha='center', va='bottom', fontsize=9)

# ✅ Adjust layout once (no need for both)
plt.tight_layout()
plt.show()
