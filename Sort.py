import pandas as pd
import os, math, time

# 160353103 rows with ending
# 160033094 rows w/o pixel ending
# 320010 pixles placed during ending

start_time = time.time()

os.system ('cls' if os.name == 'nt' else 'clear')

filename = "SmallCutSet.csv"

data = pd.read_csv(filename)

print(f"{(time.time() - start_time)} seconds to load")

data.sort_values(by = ["coordinate", "timestamp"], kind = ["heapsort", "heapsort"], ascending = [True, True], ignore_index=False, inplace=True)

data.to_csv("SortedSet.csv", index=False)

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"{math.floor(time / 60)} minutes to finish")
