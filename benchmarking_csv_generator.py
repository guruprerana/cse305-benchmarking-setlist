max_threads = 12
max_insertions = 50001

start = 5000
skip = 5000

benchmarking_output = open('output_benchmarking_tree.txt', 'r').read().split('\n')

data_coarse = []
data_fine = []

i = 0
for thread in range(1, 12):
    row_coarse = []
    row_fine = []
    for insertions in range(5000, 50001, 5000):
        row_coarse.append(int(benchmarking_output[2*i].split(" ")[-2]))
        row_fine.append(int(benchmarking_output[2*i+1].split(" ")[-2]))
        i += 1

    data_coarse.append(row_coarse)
    data_fine.append(row_fine)

import pandas as pd

data_coarse = pd.DataFrame(data_coarse, columns=list(range(start, max_insertions, skip)), index=list(range(1, max_threads)))
data_fine = pd.DataFrame(data_fine, columns=list(range(start, max_insertions, skip)), index=list(range(1, max_threads)))

with open("benchmarking_coarse.csv", "w") as f:
    data_coarse.to_csv(f)

with open("benchmarking_fine.csv", "w") as f:
    data_fine.to_csv(f)