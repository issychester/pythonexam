# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:17:47 2019

@author: isobe
"""

import argparse
from matplotlib import pyplot as plt
import numpy as np


class Tree:

    def __init__(self, scale, spacing, number_branches, multiplier):
        self.scale = scale
        self.spacing = spacing
        self.number_branches = number_branches
        self.multiplier = multiplier

    def plot_graph(self, plot_points, array, j):
        plt.plot([0, 0], [0, 1])

        length = len(array)
        position1 = length-6
        position2 = length-3

        plt.plot([plot_points[j][0], array[position1]],
                 [plot_points[j][1], array[position1+1]])
        plt.plot([plot_points[j][0], array[position2]],
                 [plot_points[j][1], array[position2+1]])

        plt.savefig('tree_np.png')

    def create_vector_to_plot(self, plot_points, array, j, spacing, scale, flag):
        angle = [(plot_points[j][2] + spacing),
                 (plot_points[j][2] - spacing)]
        angle_add = np.array([])

        for angle in angle:
            add = np.array([plot_points[j][0] + scale*np.sin(angle),
                            plot_points[j][1] + scale*np.cos(angle),
                            angle])
            angle_add = np.hstack((angle_add, add))

        array = np.concatenate((array, angle_add), axis=0)

        if flag == 0:
            pass
        else:
            self.plot_graph(plot_points, array, j)

        return array

    def create_tree(self, flag):
        scale = self.scale
        spacing = self.spacing
        number_branches = self.number_branches
        multiplier = self.multiplier
        plot_points = [[0, 1, 0]]

        for i in range(number_branches):
            array = np.array([])
            for j in range(len(plot_points)):
                array = self.create_vector_to_plot(plot_points, array, j, spacing, scale, flag)
            plot_points = array
            rows = int((len(plot_points))/3)
            plot_points = plot_points.reshape(rows, 3)
            scale *= multiplier

def main():
    arg_des = "Input the scale, spacing, number of branches and multiplier for the tree"
    parser = argparse.ArgumentParser(description=arg_des)
    parser.add_argument('scale',
                        help='alters distance between branches must be in decimal form')
    parser.add_argument('spacing',
                        help='changes the angle between branches must be in decimal form')
    parser.add_argument('number_branches',
                        help='number of branches on the tree must be in integer form')
    parser.add_argument('multiplier',
                        help='effects length of each branch must be in decimal form')
    arguments = parser.parse_args()

    scale = float(arguments.scale)
    spacing = float(arguments.spacing)
    number_branches = int(arguments.number_branches)
    multiplier = float(arguments.multiplier)

    arguments = Tree(scale, spacing, number_branches, multiplier)
    arguments.create_tree(1)

if __name__ == "__main__":
    main()
