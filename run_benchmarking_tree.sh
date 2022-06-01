#!/bin/bash

for thread in {1..11}
do
        for insertions in {5000..50001..5000}
        do
                ./tree_benchmarker $thread $insertions
        done
done
