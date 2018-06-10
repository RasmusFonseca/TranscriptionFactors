
import pandas as pd
import numpy as np
from collections import defaultdict
import json
import sys

df = pd.read_csv(sys.argv[1])

with open(sys.argv[2], encoding='utf-8-sig') as f:
    row_names = [line.strip() for line in f]

edges = defaultdict(list)

print("Processing transcription factor pairs ....")

for colidx, col in enumerate(df.columns):
    print(" > " + col)
    # if colidx >= 40:
    #     break
    for r1 in range(df.shape[0]):
        r1_importance = df[col][r1]
        if np.isnan(r1_importance) or r1_importance < 1.0:
            continue
        r1_name = row_names[r1]

        for r2 in range(r1):
            r2_importance = df[col][r2]
            if np.isnan(r2_importance) or r2_importance < 1.0:
                continue
            r2_name = row_names[r2]

            edges[(r2_name, r1_name)].append(colidx)


print("Converting to flare ....")

# Convert to flare
flare = {
    "edges": [],
    "frameDict": {str(col_idx): col_name for (col_idx, col_name) in enumerate(df.columns)}
}

for r1_name, r2_name in edges:
    flare["edges"].append({
        "name1": r1_name,
        "name2": r2_name,
        "frames": edges[(r1_name, r2_name)]
    })

with open(sys.argv[3], 'w') as f:
    json.dump(flare, f, indent=2)

