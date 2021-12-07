import pandas as pd
class Check:
    def check_bassist(self, bassist):
       """
        This function controls if the input given
        by the user (i.e. bassist's name') is present
        in the database under the bassist column.
        If you try with geddy lee, it should
        recognize that the bassist is already present
        in the original csv file.
        If you try with "Keith Richards" 
        (unless you have added it with the "inserter function") 
        the function should return that the artist is not
        present in the file.
        """
        bassist = bassist.lower()
        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
        bassists = db["Name"].str.lower()
        if bassist in bassists.values:
                return True
        return False

    def check_band(self, band):
         """
        This function controls if the input given
        by the user (i.e. a band) is present
        in the band column inside the csv file.
        If you try with "Red hot chili peppers", 
        it should return the name of the bassists, 
        while if you try with "rolling stones" the band
        of Keith Richards (unless you have added
        it with the "inserter function") the
        function should return that the band is not
        present in the file.
        """
        band = band.lower()
        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
        bands = db["Band"].str.lower()
        if band in bands.values:
            return True
        return False