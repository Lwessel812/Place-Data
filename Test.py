import pandas as pd
import os, time

# 160353103-4 rows

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

filename = "SmallCutSet.csv"

data = pd.read_csv(filename)

data.sort_values("timestamp", kind = "heapsort", ignore_index=False, inplace=True)

data.to_csv("SmallSortedSet.csv", index=False)

print(f"{(time.time() - start_time)} seconds")
