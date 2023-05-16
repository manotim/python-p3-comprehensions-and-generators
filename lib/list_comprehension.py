#!/usr/bin/env python3

def return_evens(num_list):
    evens = [x for x in (num_list) if x % 2 == 0]
    return evens
    pass

def make_exclamation(sentence_list):
    exclamation_string = [str+'!' for str in (sentence_list)]
    return exclamation_string
    pass