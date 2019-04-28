# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:32:25 2018

@author: isobe
"""

from setuptools import setup, find_packages

setup(
      name = "alchemist",
      version = "0.1.0",
      packages = find_packages(exclude=["*test"]),
      author = "Isobel Chester",
      install_requires = ["argparse", "pyyaml"],
      entry_points = {
              'console_scripts':['abracadabra = alchemist.command:main']
              }
      )