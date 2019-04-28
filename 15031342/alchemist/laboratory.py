"""
Created on Sun Nov 25 14:38:51 2018

@author: isobe
"""

import random


class Laboratory:
    def __init__(self, shelf1, shelf2):
        self.lower = shelf1
        self.upper = shelf2

    def can_react(self, substance1, substance2):
        combo1 = (substance1 == "anti" + substance2)
        combo2 = (substance2 == "anti" + substance1)
        return combo1 or combo2

    def update_shelves(self, shelf1, shelf2, substance1, substance2_index):
        index1 = shelf1.index(substance1)
        shelf1 = shelf1[:index1] + shelf1[index1+1:]
        shelf2 = shelf2[:substance2_index] + shelf2[substance2_index+1:]
        return shelf1, shelf2

    def do_a_reaction(self, shelf1, s2):
        for sub1 in shelf1:
            pos_t = [i for i, t in enumerate(s2) if self.can_react(sub1, t)]
            if not pos_t:
                continue
            else:
                sub2_index = random.choice(pos_t)
                return self.update_shelves(shelf1, s2, sub1, sub2_index)
        return shelf1, s2

    def run_full_experiment(self, argparseInput):
        shelf1 = self.lower
        shelf2 = self.upper
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction(shelf1, shelf2)
            if shelf1_new != shelf1:
                count += 1
            ended = (shelf1_new == shelf1) and (shelf2_new == shelf2)
            shelf1, shelf2 = shelf1_new, shelf2_new
        number_reactions = format(count)

        if argparseInput:
            return number_reactions
        else:
            return (shelf1, shelf2)
