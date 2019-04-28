# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:12:14 2019

@author: isobe
"""
import time
from matplotlib import pyplot as plt
from tree import Tree as Tree_original
from tree_np import Tree as Tree_np

def collect_times():
    number_iterations = 18
    time_array = []
    time_array_original = []

    for i in range(number_iterations):
        start_time = time.time()
        arguments = Tree_np(1, 0.1, i, 0.6)
        arguments.create_tree(0)
        time_array.append(time.time() - start_time)

    for i in range(number_iterations):
        start_time1 = time.time()
        arguments1 = Tree_original(1, 0.1, i, 0.6)
        arguments1.create_tree(0)
        time_array_original.append(time.time() - start_time1)

    plot1 = plt.subplot(121)
    plot1.set_title("Time taken with numpy")
    plot1.set_ylabel("Time taken (s)")
    plot1.set_xlabel("Number of Iterations")
    plot1.plot(list(range(number_iterations)), time_array)
    plot2 = plt.subplot(122)
    plot2.set_title("Time taken without numpy")
    plot2.set_ylabel("Time taken (s)")
    plot2.set_xlabel("Number of Iterations")
    plot2.plot(list(range(number_iterations)), time_array_original)

    plt.tight_layout()
    plt.savefig('perf_plot.png')

def main():
    collect_times()

if __name__ == "__main__":
    main()
