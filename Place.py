import pandas as pd
import os, time

# 160353103-4 rows

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

filename = "CutSet.csv"

data = pd.read_csv(filename)

data.sort_values("timestamp", kind = "mergesort", ignore_index=False, inplace=True)

data.to_csv("TimeSortedSet.csv", index=False)

print(f"{(time.time() - start_time)} seconds")
