import subprocess

max_threads = 9
max_insertions = 50001

start = 5000
skip = 5000

def get_benchmark_results():
    data_coarse = []
    data_fine = []
    for num_threads in range(1, max_threads):
        row_coarse = []
        row_fine = []
        for num_insertions in range(start, max_insertions, skip):
            command = ["./set_benchmarker", str(num_threads), str(num_insertions)]
            output = subprocess.run(command, capture_output=True).stdout.decode("utf-8")

            split = output.split("\n")
            row_coarse.append(int(split[0].split(" ")[-2]))
            row_fine.append(int(split[1].split(" ")[-2]))

        data_coarse.append(row_coarse)
        data_fine.append(row_fine)

    return data_coarse, data_fine

data_coarse, data_fine = get_benchmark_results()

import pandas as pd

data_coarse = pd.DataFrame(data_coarse, columns=list(range(start, max_insertions, skip)), index=list(range(1, max_threads)))
data_fine = pd.DataFrame(data_fine, columns=list(range(start, max_insertions, skip)), index=list(range(1, max_threads)))

with open("benchmarking_coarse.csv", "w") as f:
    data_coarse.to_csv(f)

with open("benchmarking_fine.csv", "w") as f:
    data_fine.to_csv(f)
