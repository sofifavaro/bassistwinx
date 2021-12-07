{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "def return_bio(bassists):\n",
    "    db = pd.DataFrame(pd.read_csv('bassistfinal.csv'))\n",
    "    bassists = list(db[\"Name\"])\n",
    "\n",
    "    if bassist in bassist:\n",
    "        print(db[\"Name\"].loc[\n",
    "            db[\"Name\"].str.lower() == bassist.lower()].values[0], \"is a/an\", db[\n",
    "                \"Nationality\"].loc[\n",
    "                    db[\"Name\"].str.lower() == bassist.lower()].values[\n",
    "                    0], \"bassist who lived in these years:\", db[\"Life\"].loc[\n",
    "                    db[\"Name\"].str.lower() == bassist.lower()].values[\n",
    "                    0], \"The artist played in\", db[\"band\"].loc[\n",
    "                        db[\"Name\"].str.lower() == bassist.lower()].values[\n",
    "                            0], \"was most famous in the\" , db[\n",
    "                                \"period\"].loc[db[\"Name\"].str.lower(\n",
    "                                    ) == bassist.lower()].values[\n",
    "                                        0], \"belongs to the genre of\",  db[\n",
    "                                            \"genre\"].loc[\n",
    "                                                db[\"Name\"].str.lower() ==\n",
    "            bassist.lower()].values[0], \"also played or is a solist\", db[\n",
    "                \"solist\"].loc[db[\"Name\"].str.lower() == bassist.lower()].values[\n",
    "                    0], \"has a stage name\", db[\"stage name\"].loc[\n",
    "                        db[\"Name\"].str.lower() == bassist.lower(\n",
    "                            )].values[0], \"Here you can find\" +\n",
    "                                          \" the web link\" +\n",
    "                                          \" to see\" +\n",
    "                                          \" the complete biography: \", db[\n",
    "                                          \"wikipedia\"].loc[db[\n",
    "                                              \"Name\"].str.lower(\n",
    "                                              ) == bassist.lower()].values[0])\n",
    "    else:\n",
    "        print(bassist + \" seems not to be present in our database.\" +\n",
    "                       \"Are you sure that you wrote\" +\n",
    "                       \" the name of the artist correctly?\" +\n",
    "                       \" Use -d to check if it is already in our database,\" +\n",
    "                       \"maybe there is a spelling error in the input.\" +\n",
    "                       \" Check it and then try again, if it is not present,\" +\n",
    "                       \"use -a to insert the new artist,\" +\n",
    "                       \" thank you for your patience!\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "The function of the biography module\n",
    "is to explain, in a more understandable way,\n",
    "who was the artist with relative\n",
    "most famous painting, the number of artworks that\n",
    "has been made, movement, day of birth and death\n",
    "that can be found into our database.\n",
    "The function first checks if the input\n",
    "the user inserted is present in\n",
    "the database, if not the system will warn the user\n",
    "and invite him to check if it is correctly written.\n",
    "The user can also read and see the full biography with\n",
    "the Wikipedia's link.\n",
    "\"\"\"\n",
    "    \"\"\"\n",
    "    This function comes into play once the user inputs a value\n",
    "    and wants to obtain as output the complete list of information that\n",
    "    can be found inside the database, or when, after\n",
    "    the input, the user writes the optional argument -bio.\n",
    "    It recognizes the input if it is a name of an artist.\n",
    "    \"\"\""
   ]
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
