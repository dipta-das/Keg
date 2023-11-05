#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 19:06:13 2023

@author: diptadas
"""

help(print)

def least_difference(a,b,c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

least_difference(340, 380, 430)

help(least_difference)

print(1,2,3, sep = '<')


def greet(who = "Colin"):
    print("Hello, ", who, "!")
    

greet()
greet("Dipta")
greet("Arif")


def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    return fn(arg)


help(round)

""" Ndigit which is the second parameter of round
If i use that as -1, -2, -3 and 
ndigits=-1 rounds to the nearest 10, ndigits=-2 rounds to the nearest 100"""

print("The area of Finland is 338424 km²")
print("The area of Finland is ",round(338424,-3)," km²")
