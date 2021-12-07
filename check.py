import pandas as pd
class Check:
    def check_bassist(self, bassist):
       
        bassist = bassist.lower()
        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
        bassists = db["Name"].str.lower()
        if bassist in bassists.values:
                return True
        return False

    def check_band(self, band):
        
        band = band.lower()
        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))
        bands = db["Band"].str.lower()
        if band in bands.values:
            return True
        return False