# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:39:11 2018

@author: isobe
"""

import yaml
import argparse
from alchemist.laboratory import Laboratory
import sys

def modify_input(input):
    if input is None:
        raise Exception('File empty')

    input = {k.lower(): v for k, v in input.items()}

    if len(input) != 2:
        if len(input) > 2:
            raise Exception('There cannot be more than 2 shelves')
        else:
            raise Exception('There has to be at least 2 shelves')
    if input['upper'] is None:
        input['upper'] = ['none']
    if input['lower'] is None:
        input['lower'] = ['none']
    if any("antianti" in shelf for shelf in input['lower']):
        raise Exception('antianti products do not exist! There is one in the lower shelf')
    if any("antianti" in shelf for shelf in input['upper']):
        raise Exception('antianti products do not exist! There is one in the upper shelf')

    input['upper'] = [k.lower() for k in input['upper']]
    input['lower'] = [k.lower() for k in input['lower']]

    return input

def main():
    argDes = "Whether output is the substances left on shelves or number of reactions"
    parser = argparse.ArgumentParser(description=argDes)
    parser.add_argument('file')
    parser.add_argument('--reactions', '--r', help='/n/', action='store_true', dest='reactions')
    arguments = parser.parse_args()

    try:
        input = yaml.load(open(arguments.file))
    except IOError:
        print("File cannot be opened")

    input = modify_input(input)

    inputShelf = Laboratory(input['lower'], input['upper'])
    d = inputShelf.run_full_experiment(arguments.reactions)
    if arguments.reactions:
        d_dump = yaml.dump(d)
        d_load = yaml.load(d_dump)
        return sys.stdout.write(d_load)
    else:
        dict = {"lower": d[0],
                "upper": d[1]}
        return yaml.dump(dict, sys.stdout)

if __name__ == "_main_":
    main()
