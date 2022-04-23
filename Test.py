import pandas as pd
import os, math, time

# 160353103-4 rows

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

filename = "SmallSortedSet.csv"

data = pd.read_csv(filename)

print(f"{(time.time() - start_time)} seconds to load")

data.sort_values("timestamp", kind = "heapsort", ignore_index=False, inplace=True)

data.to_csv("SmallSortedSet.csv", index=False)

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"{math.floor(time / 60)} minutes to finish")
