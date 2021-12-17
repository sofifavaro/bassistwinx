"""
This module is aimed to tests some of the functions
necessary to let the user interact with the database.
Each Test Case tests a valid and invalid entries,
to see what the program do.
TearDown and SetUp functions were used as well
to set up mock variables and the csv file needed
to test the functions.
"""

import unittest
from check import Check
import inserter as ins
import similarities as sim
import pandas as pd


class TestName(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
        print(db)
        ind = db.loc[db["Name"] == "Alessandro Federigo"].index.values
        db.drop(db.index[ind[:]], inplace=True)
        db.to_csv("bassistsfinal.csv", index=False)

    def setUp(self):
        self.T_bassist = "Flea"
        self.T_band = "Red Hot Chili Peppers"
        self.F_bassist = "Cristoforo Colombo"
        self.F_band = "Nina"
        self.new_bassist = "Alessandro Federigo"
        self.database = "bassistsfinal.csv"
        self.column = "Nationality"
        self.parameter = "Italian"

    def test_wrong_check_bassist(self):
        self.assertFalse(Check().check_bassist(self.F_bassist))
        self.assertFalse(Check().check_bassist(self.T_band))
        self.assertFalse(Check().check_bassist(self.F_band))

    def test_wrong_check_band(self):
        self.assertFalse(Check().check_band(self.T_bassist))
        self.assertFalse(Check().check_band(self.F_band))

    def test_inserter(self):
        test1 = print("Sorry, but " + self.T_bassist +
                      " is already present in the database, thank you anyway")

        test2 = print("Sorry, but " + self.F_band +
                      " is not present in the database, thank you anyway")

        test3 = print("Thank you for your contribution!")

    def test_correct_similarities(self):
        self.assertEqual(sim.similarities(self.column, self.parameter), None)

# by setting this up we can run this file
# on the command line without having
# having to call the unittest module.


if __name__ == "__main__":
    unittest.main()
