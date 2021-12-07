import pandas as pd

def similarities(column, parameter):
    """
    This function returns similarities between the
    bassist given as an input and
    the other bassists stored in our database.
    The code is structured in order to
    individuate similarities according to columns
    "Nationality", "Genre" and "period".
    The user should select the column she/he
    is interested in.
    If the user is looking for similarities according
    to the period,
    she/he is asked to specify if she/he is interested
    in a period after, before or equal period.
    """
    db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))

    column = str(column)

    if type(parameter) == int:
        valore = str(input("Do you want to search for period " +
                           "that was after (>), before (<) or " +
                           "the same (==) period you provided as input?"))

        if valore == ">":
            result = db.loc[db[column] > parameter][["Name", column]]
            if len(result) > 1:
                print("The bassists that were famous after " +
                      "than {}s are the following: {}".format(
                       parameter, result))
            else:
                print("Sorry, there are no bassists that were famous " +
                      "after {}s .".format(parameter))

        elif valore == "<":
            result = db.loc[db[column] < parameter][["Name", column]]
            if len(result) > 1:
                print("The artists that were famous before " +
                      "than {}s are the following:{}".format(
                       parameter, result))
            else:
                print("Sorry, there are no bassists that were famous " +
                      "before {}s artworks. ".format(parameter))
        elif valore == "==":
            result = db.loc[db[column] == parameter][["Name", column]]
            if len(result) > 1:
                print("The bassists that were famous in the same period " +
                      "{}s are the following: {}".format(
                       parameter, result))
            elif len(result) == 1:
                print("The bassists that was famous in the same period " +
                      "{}s is the following: {}".format(
                       parameter, result))
            else:
                print("Sorry, there are no bassists that were famous" +
                      "in this period {} ".format(parameter))
        else:
            print("You have to enter <, > or ==.")

    else:
        parameter = str(parameter)
        result = db.loc[db[column] == parameter][["Name"]]
        if column == ("Nationality"):
            if len(result) > 1:
                print("{} bassists are the following:{}".format(
                       parameter, result))
            else:
                print("Sorry, there are not {} bassists ".format(parameter))
        else:
            if len(result) > 1:
                print("Bassists belonging to "
                      "{} genre are the following: {}".format(
                       parameter, result))
            else:
                print("Sorry, there are not bassists " +
                      "belonging to {} genre ".format(parameter))
    