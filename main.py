"""
This is the main file where we created
the interaction between the user and the
database of bassists.
We used the argparse module to configure
all the positional and optional arguments.
Depending on the arguments given,
the program leads the user to a series of steps
to either check the presence of bassist or of the
band inside the database and/or add them to it.
There is also the possibility to check out
the association between bassists and bands.
"""

from inserter import add_element
from check import Check 
from similarities import similarities
from bio import return_bio
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
parser = argparse.ArgumentParser(description='This program will' +
                                             ' check if the name you put is' +
                                             ' inside our database of ' +
                                             'bassists and the ' +
                                             'band in which they play.' +
                                             ' If the names have ' +
                                             'more than one space, ' +
                                             'wrap them ' +
                                             'around quotes ("").')
group = parser.add_mutually_exclusive_group()
group.add_argument("-bio", "--biography", action="store_true",
                   help="entire biography of the bassist")
args = parser.parse_args()
answer = args.name