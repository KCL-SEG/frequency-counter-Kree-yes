"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for i in items:
        i = str(i)
        if (frequencies.get(i) != None):
            frequencies[i] = frequencies[i] + 1
        else:
            frequencies[i] = 1
    
    return frequencies
