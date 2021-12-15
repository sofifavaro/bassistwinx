"""
The function of the bio module
is to explain, in the most understandable way possible,
who was the bassist with his/her relative
band in which he/she played, when he/she lived,
if he/she had a stage name,
the genre they played, his/her nationality,
if he/she played as a solist or not,
and the period in which he/she was most famous.
The function first checks if the input
the user inserted is present in
the database, if not the system will warn the user
and invite him/her to check if it is correctly written.
The user can also read and see the full biography with
the Wikipedia's link.
"""

import pandas as pd


def return_bio(bassist):
    """
    This function comes into play once the user inputs a value
    and wants to obtain as output the complete list of information that
    can be found inside the database, or when, after
    the input, the user writes the optional argument -bio.
    It recognizes the input if it is a name of a bassist.
    """
    db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
    bassists = list(db["Name"])

    if bassist in bassists:
        print(db["Name"].loc[
            db["Name"].str.lower() == bassist.lower()].values[
            0], "is a/an", db[
                "Nationality"].loc[
                    db["Name"].str.lower() == bassist.lower()].values[
                    0], "bassist who lived in these years:", db["Life"].loc[
                    db["Name"].str.lower() == bassist.lower()].values[
                    0], "The artist played in", db["Band"].loc[
                        db["Name"].str.lower() == bassist.lower()].values[
                            0], " and he/she was most famous in the", db[
                                "Period"].loc[db["Name"].str.lower(
                                    ) == bassist.lower()].values[
                                        0], "s. He/She belongs to
                                        the genre of", db[
                                            "Genre"].loc[
                                                db["Name"].str.lower() ==
            bassist.lower()].values[0], "He/She", db[
                "Solist"].loc[db["Name"].str.lower() ==
                 bassist.lower()].values[
                    0], "played as a soloist, and He/She", db[
                    "Stage Name"].loc[
                        db["Name"].str.lower() == bassist.lower(
                            )].values[0], "a stage name. Here you can find" +
                                          " the web link" +
                                          " to see" +
                                          " the complete biography: ", db[
                                          "Wikipedia"].loc[db[
                                              "Name"].str.lower(
                                              ) == bassist.lower()].values[0])
    else:
        print(bassist + " seems not to be present in our database." +
                        "Are you sure that you wrote" +
                        " the name of the artist correctly?" +
                        " Use -d to check if it is already in our database," +
                        "maybe there is a spelling error in the input." +
                        " Check it and then try again, if it is not present," +
                        "use -a to insert the new artist," +
                        " thank you for your patience!")
