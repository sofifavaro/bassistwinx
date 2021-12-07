import pandas as pd

def return_bio(bassist):
    db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
    bassists = list(db["Name"])

    if bassist in bassists:
        print(db["Name"].loc[
            db["Name"].str.lower() == bassist.lower()].values[0], "is a/an", db[
                "Nationality"].loc[
                    db["Name"].str.lower() == bassist.lower()].values[
                    0], "bassist who lived in these years:", db["Life"].loc[
                    db["Name"].str.lower() == bassist.lower()].values[
                    0], "The artist played in", db["Band"].loc[
                        db["Name"].str.lower() == bassist.lower()].values[
                            0], " and he/she was most famous in the" , db[
                                "Period"].loc[db["Name"].str.lower(
                                    ) == bassist.lower()].values[
                                        0], "s. He/She belongs to the genre of",  db[
                                            "Genre"].loc[
                                                db["Name"].str.lower() ==
            bassist.lower()].values[0], "He/She", db[
                "Solist"].loc[db["Name"].str.lower() == bassist.lower()].values[
                    0], "played as a soloist, and He/She", db["Stage Name"].loc[
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