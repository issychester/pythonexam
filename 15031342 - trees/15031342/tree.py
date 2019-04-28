# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 21:40:19 2019

@author: isobe
"""

from math import sin, cos
import argparse
from matplotlib import pyplot as plt


class Tree:

    def __init__(self, scale, spacing, number_branches, multiplier):
        self.scale = scale
        self.spacing = spacing
        self.number_branches = number_branches
        self.multiplier = multiplier

    def plot_graph(self, plot_points, array, j):
        array_position = [-2, -1]

        for position in array_position:
            plt.plot([plot_points[j][0], array[position][0]],
                     [plot_points[j][1], array[position][1]])

    def create_vector_to_plot(self, plot_points, array, j, spacing, scale, flag):
        angle = [(plot_points[j][2] + spacing),
                 (plot_points[j][2] - spacing)]

        for angle in angle:
            array.append([plot_points[j][0]+scale*sin(angle),
                          plot_points[j][1]+scale*cos(angle), 
                          angle])

        if flag == 0:
            pass
        else:
            plt.plot([0, 0], [0, 1])
            plt.savefig('tree.png')
            self.plot_graph(plot_points, array, j)

    def create_tree(self, flag):
        scale = self.scale
        spacing = self.spacing
        number_branches = self.number_branches
        multiplier = self.multiplier
        plot_points = [[0, 1, 0]]

        for i in range(number_branches):
            array = []
            for j in range(len(plot_points)):
                self.create_vector_to_plot(plot_points, array, j, spacing, scale, flag)
            plot_points = array
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
