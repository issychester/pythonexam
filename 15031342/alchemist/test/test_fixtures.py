# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:20:25 2018

@author: isobe
"""

import pytest
from alchemist.laboratory import Laboratory
from alchemist import command
import yaml
import os
#from mock import patch 
#import sys
#import mock

path = os.path.join(os.path.dirname(__file__), 'fixtures.yml')
path = open(path, 'r')
input = yaml.load(path)
path.close

dataMultiLabs = [(input["lab1"]["input"]['lower'], input["lab1"]["input"]["upper"], input["lab1"]["expected"]["lower"], input["lab1"]["expected"]["upper"], '2' ),
                 (input["lab2"]["input"]['lower'], input["lab2"]["input"]["upper"], input["lab2"]["expected"]["lower"], input["lab2"]["expected"]["upper"], '2' ),
                 (input["lab3"]["input"]['lower'], input["lab3"]["input"]["upper"], input["lab3"]["expected"]["lower"], input["lab3"]["expected"]["upper"], '2' ),
                 (input["lab4"]["input"]['lower'], input["lab4"]["input"]["upper"], input["lab4"]["expected"]["lower"], input["lab4"]["expected"]["upper"], '1' ) ]
reaction = [(input["reaction"]["input"]['lower'], input["reaction"]["input"]["upper"], input["reaction"]["expected"]["lower"], input["reaction"]["expected"]["upper"])]
updateShelves = [(input["update_shelves"]["input"]['lower'], input["update_shelves"]["input"]["upper"], input["update_shelves"]["expected"]["lower"], input["update_shelves"]["expected"]["upper"])]
threeShelves = [(input["three_shelves"]["input"]['lower'], input["three_shelves"]["input"]["upper"], input["three_shelves"]["input"]["middle"])]
oneShelf = [(input["one_shelf"]["input"]['lower'], input["three_shelves"]["input"]["upper"])]
emptyShelfUpper = [(input["empty_shelf_upper"]["input"]['lower'], input["empty_shelf_upper"]["input"]["upper"], input["empty_shelf_upper"]["expected"]["lower"], input["empty_shelf_upper"]["expected"]["upper"])]
emptyShelfLower = [(input["empty_shelf_lower"]["input"]['lower'], input["empty_shelf_lower"]["input"]["upper"], input["empty_shelf_lower"]["expected"]["lower"], input["empty_shelf_lower"]["expected"]["upper"])]
antiLowerShelf = oneShelf = [(input["anti_lower_shelf"]["input"]['lower'], input["anti_lower_shelf"]["input"]["upper"])]
antiUpperShelf = oneShelf = [(input["anti_upper_shelf"]["input"]['lower'], input["anti_upper_shelf"]["input"]["upper"])]
antiBothShelves = [(input["anti_both_shelves"]["input"]['lower'], input["anti_both_shelves"]["input"]["upper"])]
uppercaseLower = [(input["uppercase_lower"]["input"]['lower'], input["uppercase_lower"]["input"]["upper"], input["uppercase_lower"]["expected"]["lower"], input["uppercase_lower"]["expected"]["upper"])]
uppercaseUpper = [(input["uppercase_upper"]["input"]['lower'], input["uppercase_upper"]["input"]["upper"], input["uppercase_upper"]["expected"]["lower"], input["uppercase_upper"]["expected"]["upper"])]
lowerUppercase = [(input["lower_uppercase"]["input"]['LOWER'], input["lower_uppercase"]["input"]["upper"], input["lower_uppercase"]["expected"]["lower"], input["lower_uppercase"]["expected"]["upper"])]
upperUppercase = [(input["upper_uppercase"]["input"]['lower'], input["upper_uppercase"]["input"]["UPPER"], input["upper_uppercase"]["expected"]["lower"], input["upper_uppercase"]["expected"]["upper"])]
ordered = [(input["order"]["input"]["lower"], input["order"]["input"]["upper"], input["order"]["output"]["lower1"], input["order"]["output"]["lower2"], input["order"]["output"]["upper"])]
empty = [input["empty"]]

class TestSample(object): 
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", reaction)
    def test_do_a_reaction(self, lower, upper, expected_lower, expected_upper):
        e = Laboratory(lower, upper)
        outcome = e.do_a_reaction(lower, upper)
        assert outcome[0] == expected_lower
        assert outcome[1] == expected_upper
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper, count", dataMultiLabs)
    def test_positive(self, lower, upper, expected_lower, expected_upper, count):
        outcome=Laboratory(lower,upper)
        d = outcome.run_full_experiment(0)
        f = outcome.run_full_experiment(1)
        
        assert f==(count)        
        assert d==(expected_lower, expected_upper)
        
    def test_can_react(self):
        outcome=Laboratory.can_react(0,'coffee', 'anticoffee')
        assert outcome == True
        
    def test_can_react_false(self):
        outcome=Laboratory.can_react(0,'coffee', 'tea')      
        assert outcome == False
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper",updateShelves)
    def test_update_shelves(self, lower, upper, expected_lower, expected_upper):
        outcome = Laboratory.update_shelves(self, lower, upper, 'tea', 2)
        assert outcome[0] == expected_lower
        assert outcome[1] == expected_upper
        
    @pytest.mark.parametrize("lower, upper, middle", threeShelves)        
    def test_error_with_more_than_two_shelves(self, lower, upper, middle):        
        with pytest.raises(Exception) as e:
            e = Laboratory(lower, upper, middle)
            
    @pytest.mark.parametrize("lower, upper", oneShelf)    
    def test_error_with_one_shelf(self, lower, upper):
        with pytest.raises(Exception) as e:
            e = Laboratory(lower)
            
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper, count", dataMultiLabs)
    def test_positive_main(self, lower, upper, expected_lower, expected_upper, count):
        outcome = command.main
        assert outcome
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", emptyShelfUpper)
    def test_empty_upper_shelf_has_none_allocated(self, lower, upper, expected_lower, expected_upper):
        outcome = command.modify_input({"lower": lower, "upper": upper})
        assert outcome == {"lower": expected_lower, "upper": expected_upper}
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", emptyShelfLower)
    def test_empty_lower_shelf_has_none_allocated(self, lower, upper, expected_lower, expected_upper):
        outcome = command.modify_input({"lower": lower, "upper": upper})
        assert outcome == {"lower": expected_lower, "upper": expected_upper}
        
    @pytest.mark.parametrize("lower, upper, middle", threeShelves)        
    def test_error_raised_in_command_with_more_than_two_shelves(self, lower, upper, middle):        
        with pytest.raises(Exception) as e:
            e = command.modify_input({"lower": lower, "upper": upper, "middle": middle})
            
    @pytest.mark.parametrize("lower, upper", oneShelf)    
    def test_error_with_one_shelf(self, lower, upper):
        with pytest.raises(Exception) as e:
            e = command.modifiyInput({"lower":lower, "upper": upper})
    
    @pytest.mark.parametrize("lower, upper", antiLowerShelf)        
    def test_error_raised_in_command_with_antianti_in_lower(self, lower, upper):        
        with pytest.raises(Exception) as e:
            e = command.modify_input({"lower": lower, "upper": upper})

    @pytest.mark.parametrize("lower, upper", antiUpperShelf)        
    def test_error_raised_in_command_with_antianti_in_upper(self, lower, upper):        
        with pytest.raises(Exception) as e:
            e = command.modify_input({"lower": lower, "upper": upper})
            
    @pytest.mark.parametrize("lower, upper", antiBothShelves)        
    def test_error_raised_in_command_with_antianti_in_upper(self, lower, upper):        
        with pytest.raises(Exception) as e:
            e = command.modify_input({"lower": lower, "upper": upper})
            
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper, count", dataMultiLabs)
    def test_reactions_output_is_number(self, lower, upper, expected_lower, expected_upper, count):
        outcome=Laboratory(lower,upper)
        d = outcome.run_full_experiment(1)
        assert type(d) == str
    
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper, count", dataMultiLabs)
    def test_output_is_tuple(self, lower, upper, expected_lower, expected_upper, count):
        outcome=Laboratory(lower,upper)
        d = outcome.run_full_experiment(0)
        assert type(d) == tuple
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", uppercaseLower)
    def test_inputs_in_lower_shelf_are_made_lowercase(self, lower, upper, expected_lower, expected_upper):
        outcome = command.modify_input({"lower": lower, "upper": upper})
        assert outcome == {"lower": expected_lower, "upper": expected_upper}
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", uppercaseUpper)
    def test_inputs_in_upper_shelf_are_made_lowercase(self, lower, upper, expected_lower, expected_upper):
        outcome = command.modify_input({"lower": lower, "upper": upper})
        assert outcome == {"lower": expected_lower, "upper": expected_upper}
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", lowerUppercase)
    def test_with_uppercase_lower_shelf_name(self, lower, upper, expected_lower, expected_upper):
        outcome = command.modify_input({"lower": lower, "upper": upper})
        assert outcome == {"lower": expected_lower, "upper": expected_upper}
        
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper", upperUppercase)
    def test_with_uppercase_upper_shelf_name(self, lower, upper, expected_lower, expected_upper):
        outcome = command.modify_input({"lower": lower, "upper": upper})
        assert outcome == {"lower": expected_lower, "upper": expected_upper}
        
    @pytest.mark.parametrize("lower, upper, lower1, lower2, expected_upper", ordered)
    def test_different_ordered_output_shelves_are_correct(self, lower, upper, lower1, lower2, expected_upper):
        outcome=Laboratory(lower,upper)
        d = outcome.run_full_experiment(0)
        assert d[0] == (lower1 or lower2)
        assert d[1] == expected_upper
        
    @pytest.mark.parametrize("input", empty)
    def test_empty_file_throws_error(self, input):
        with pytest.raises(Exception) as e:
            e = command.modify_input(input)
    
    @pytest.mark.parametrize("lower, upper, expected_lower, expected_upper, count", dataMultiLabs)
    def test_error_thrown_with_invalid_arguments_in_argparse(self, lower, upper, expected_lower, expected_upper, count):
        outcome = Laboratory(lower, upper)
        with pytest.raises(Exception) as e:
            e = outcome.run_full_experiment(0, --a)