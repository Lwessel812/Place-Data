# This file sorts the data, Strip the data first unless you want to wait forever

import pandas as pd
import os, math, time

start_time = time.time()

os.system ("cls" if os.name == "nt" else "clear") # Clear console

filename = "C:\Temp\PlaceHistory\ProcessedSet.csv"  # Name/Path of file being imported

data = pd.read_csv(filename, low_memory = False, dtype= {"coordinate": "str", "timestamp": "str"}) # Import file into Pandas dataframe

print(f"{(time.time() - start_time)} seconds to load")

data.sort_values(by = ["coordinate", "timestamp"], kind = ["mergesort", "mergesort"], ignore_index=False, inplace=True) # Sort the data by both the cordinate and timestamp columns, mergesort is the fastest sort I found for data sets this large that pandas can do

data.to_csv("C:\Temp\PlaceHistory\SortedSet.csv", index=False) # Save the new sorted file to another file

time = (time.time() - start_time)
print(f"{time} seconds to finish")
print(f"{math.floor(time / 60)} minutes to finish")
