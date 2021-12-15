
"""
The function of the inserter module
allows to append new bassists with relative
bands into our database.
The function first checks if the input
the user wants to insert is already present in
the database, if not it asks if the inserted
value is the name of a bassist
or the name of a band.
After that it requires to add all the
other additional information, to generate
a list of 9 items.
Finally the list is inserted in a new
row becoming part
of our database.
"""


import csv
import pandas as pd
from check import Check
from csv import writer


def add_element(a_or_b, response=""):

    """
    This function comes into play once the user inputs a value
    that is not inside the database, or when, after
    the input, the user writes the optional argument -a.
    It asks if the input is a name of a bassist or a band,
    then it asks for the remaining values to insert in all the 9 columns
    of the database.
    """

    db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))

    if Check().check_bassist(a_or_b):
        return print("Sorry, but " + a_or_b + " is already present " +
                     "in the database, thank you anyway")
    elif Check().check_band(a_or_b):
        return print("Sorry, but " + a_or_b + " is already " +
                     "present in the database. {} is part of the band {}."
                     .format(a_or_b, db["Name"].loc[
                         db["Band"].str.lower() == a_or_b.lower()]
                             .values[0]))
    else:
        name1 = input(
            "Is he/she a bassist or is it the name of a band (a or b) -> ")

        if name1 == "a":
            if response == "":
                name2 = input(
                    "Now enter the full name of the bassist -> ")
                while(name2 == ""):
                    name2 = input("You can't enter nothing... " +
                                  "so please... put anything -> ")
            band = input(
                "Now enter the name of the band of the bassist->")
            while(band == ""):
                band = input(
                    "You can't enter nothing..." + "please put anything ->")
            genre = input(
                "Now enter the music genre of the bassist->")
            while(genre == ""):
                genre = input(
                    "You can't enter nothing..." + "please put anything ->")
            nationality = input(
                "Now enter the nationality of the bassist->")
            while(nationality == ""):
                nationality = input(
                    "You can't enter nothing..." + "please put anything ->")
            life = input(
                "Now enter the life period of the bassist->")
            while(life == ""):
                life = input(
                    "You can't enter nothing..." + "please put anything ->")
            stagename = input(
                "Now enter 'has' or 'has not' depending on whether the" +
                "bassist had a stage name or not ->")
            while(stagename == ""):
                stagename = input(
                    "You can't enter nothing..." + "please put anything ->")
            solist = input(
                "Now enter 'only' or 'never' or 'sometimes' depending on" +
                "whether the bassist was only, sometimes or never a solist->")
            while(solist == ""):
                solist = input(
                    "You can't enter nothing..." + "please put anything ->")
            period = input(
                "Now enter the time period during which the bassist" +
                "was most famous or successful->")
            while(period == ""):
                period = input(
                    "You can't enter nothing..." + "please put anything ->")
            wiki = input(
                "Now enter the link to the wikipedia page of the bassist->")
            while(wiki == ""):
                wiki = input(
                    "You can't enter nothing..." + "please put anything ->")

            with open(r'artists_paintings.csv', 'a') as write_obj:
                writer = csv.writer(write_obj)
                row = len(db)
                write_obj.write("\n")
                writer.writerow([row, name2, genre, a_or_b, nationality,
                                 solist, genre, nationality, stagename, wiki])
                write_obj.close()
            return print("Thank you for your contribution!")

        elif name1 == "b":
            if response == "":
                name1 = input("Now enter the name of the bassist -> ")
                while(name1 == ""):
                    name1 = input("You can't enter nothing..." +
                                  "so please... put anything -> ")
            band = input(
                "Now enter the name of the band of the bassist->")
            while(band == ""):
                band = input(
                    "You can't enter nothing..." + "please put anything ->")
            genre = input(
               "Now enter the music genre of the bassist->")
            while(genre == ""):
                genre = input(
                    "You can't enter nothing..." + "please put anything ->")
            nationality = input(
                "Now enter the nationality of the bassist->")
            while(nationality == ""):
                nationality = input(
                    "You can't enter nothing..." + "please put anything ->")
            life = input(
                "Now enter the life period of the bassist->")
            while(life == ""):
                life = input(
                    "You can't enter nothing..." + "please put anything ->")
            stagename = input(
                "Now enter 'has' or 'has not' depending on whether the" +
                "bassist had a stage name or not ->")
            while(stagename == ""):
                stagename = input(
                    "You can't enter nothing..." + "please put anything ->")
            solist = input(
               "Now enter 'only' or 'never' or 'sometimes' depending on" +
               "whether the bassist was only, sometimes, never a solist->")
            while(solist == ""):
                solist = input(
                    "You can't enter nothing..." + "please put anything ->")
            period = input(
                "Now enter the time period during which the bassist was" +
                "most famous or successful->")
            while(period == ""):
                period = input(
                    "You can't enter nothing..." + "please put anything ->")
            wiki = input(
                "Now enter the link to the wikipedia page of the bassist->")
            while(wiki == ""):
                wiki = input(
                    "You can't enter nothing..." + "please put anything ->")

            with open(r'artists_paintings.csv', 'a') as write_obj:
                writer = csv.writer(write_obj)
                row = len(db)
                write_obj.write("\n")
                writer.writerow([row, name1, genre, a_or_b, nationality,
                                 solist, genre, nationality, stagename, wiki])
                write_obj.close()
            return print("Thank you for your contribution!")
        else:
            return input("You need to input a or p")
