{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "class check:\n",
    "    def check_bassist(self, bassist):\n",
    "        \"\"\"\n",
    "        This function controls if the input given\n",
    "        by the user (i.e. bassist's name') is present\n",
    "        in the database under the bassist column.\n",
    "        If you try with geddy lee, it should\n",
    "        recognize that the bassist is already present\n",
    "        in the original csv file.\n",
    "        If you try with \"Keith Richards\" \n",
    "        (unless you have added it with the \"inserter function\") \n",
    "        the function should return that the artist is not\n",
    "        present in the file.\n",
    "        \"\"\"\n",
    "        bassist = bassist.lower()\n",
    "        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))\n",
    "        bassists = db[\"Name\"].str.lower()\n",
    "        if bassist in bassists.values:\n",
    "                return True\n",
    "        return False\n",
    "\n",
    "    def check_band(self, band):\n",
    "        \"\"\"\n",
    "        This function controls if the input given\n",
    "        by the user (i.e. a band) is present\n",
    "        in the band column inside the csv file.\n",
    "        If you try with \"Red hot chili peppers\", \n",
    "        it should return the name of the bassists, \n",
    "        while if you try with \"rolling stones\" the band\n",
    "        of Keith Richards (unless you have added\n",
    "        it with the \"inserter function\") the\n",
    "        function should return that the band is not\n",
    "        present in the file.\n",
    "        \"\"\"\n",
    "        band = band.lower()\n",
    "        db = pd.DataFrame(pd.read_csv('bassistsfinal.csv'))\n",
    "        bands = db[\"Band\"].str.lower()\n",
    "        if band in bands.values:\n",
    "            return True\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
