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
parser.add_argument("name",
                    help="input the name of a known bassist or band")
group.add_argument("-a", "--add", action="store_true",
                   help="add a new bassist or band")
group.add_argument("-d", "--database", action="store_true",
                   help="show bassist and relative band")
group.add_argument("-bio", "--biography", action="store_true",
                   help="entire biography of the bassist")
group.add_argument("-b", "--bands", action="store_true",
                   help="show the list of bands")
group.add_argument("-bas", "--bassist", action="store_true",
                   help="show the list of bassists")
group.add_argument("-s", "--similarities", action="store_true",
                   help="show similar bassists by nat/gen/per")
args = parser.parse_args()
answer = args.name

check = Check()

if args.bands:
    print("Now you can see by yourself if the band " +
          "is present in our database!")
    print(db["Band"])
elif args.bassist:
    print("Now you can see by yourself if the bassist " +
          "is present in our database!")
    print(db["Name"])

if args.similarities:
    response2 = input("Do you want to see the similarities according " +
                      "to nationality, genre or period of " +
                      "activities? (nat, gen, per) -> ")
    if response2 == "nat":
        similarities("Nationality", db.loc[
            db['Name'] == answer, 'Nationality'].iloc[0])
    elif response2 == "gen":
        similarities("Genre", db.loc[db['Name'] == answer, 'Genre'].iloc[0])
    else:
        similarities("Period", int(db.loc[
            db['Name'] == answer, 'Period'].iloc[0]))
elif args.database:
    print("Now you can see by yourself if the bassist and his/her " +
          "band are present in our database!")
    print(db["Name"] + " : " + db["Band"])

elif args.biography:
    return_bio(answer)

elif args.database:
    print("Now you can see by yourself if the bassist and his/her " +
          "band are present in our database!")
    print(db["Name"] + " : " + db["Band"])
else:
    if args.add:
        add_element(answer)
    elif check.check_band(answer):
        print("The bassist of", db["Band"]
              .loc[db["Band"].str.lower() == answer.lower()].values[0],
              "is", db["Name"].loc[db["Band"].str.lower() ==
              answer.lower()].values[0])
    elif check.check_bassist(answer):
        print(db["Name"].loc[db["Name"].str.lower() == answer.lower()]
              .values[0], "is the bassist of",
              db["Band"].loc[db["Name"].str.lower() ==
              answer.lower()].values[0])
    else:
        response = input(answer + " is not present in our database. Are you " +
                         "sure that you wrote it correctly " +
                         "(use -d to check if it is " +
                         "already in our database)?(y or n) -> ")
        if response == "y":
            response1 = input(
                "Great! Do you want to add he/her/it? (y or n) -> ")
            if response1 == "y":
                add_element(answer)
            else:
                print("Thank you anyway")
        else:
            print("Use -d to check if it is already in our database, " +
                  "maybe there is a spelling error in the input. " +
                  "Then try again, thank you for your patiance!")
