# Bassist project goal🎸


BassistWinx is a software development project that allows users to obtain information about famous bassists and their bands, if they played in any. 

If the name of the bassist or band given as input is not present or not available, the program asks the user whether he/she wants to insert it. All of this can be managed directly from the user's machine terminal.

# CSV file📃

We have decide to create e CSV file called `bassistfinal.csv` , instead of working with an enormous list of bassists inside the main function. 
The CSV file contains 9 columns which are:

 - **Name** contains name and surname of the bassist
 - **Band** contain the name of the band if he/she played in one
 - **Nationality** of the bassists 
 - **Genre** music that they mainly play
 - **Life** period in which they were alive
 - **Stage Name** if the bassist had it or not 
 - **Solist** if the bassist have played as solist 
 - **Period** the period in which the bassist was more famous
 - **Wikipedia** the link to the wikipidia page

Our original file CSV contains 34 rows, which correspond to the bassists.

# How to start👩🏼‍💻

To start you just need to clone the remote directory in the terminal of your computer by copy this command: 
`git clone https://github.com/sofifavaro/bassistwinx.git`

This will automatically download all the files the user needs to run the program.

# Functionalities ⚙️

In order to develop a suitable structure for our project according to the intended goals, we created 4 main functions and stored them into different modules:

 - `add_element` function;
 - `check_bassist` and `check_band` functions;
 - `similarities` function;
 - `return_bio` function.

All these functions are called by argparse from the `main.py` module by the corresponding optional arguments.

If you just want to execute the program, you just need to write the command as follow:
`python main.py "name"`

The name of the bassist or painting is indeed a positional argument that should always be included.
Let's see a pratical example, if we wrote in our terminal:

    python main.py "Flea"
The result we will see is:

    Flea is the bassist of Red Hot Chili Peppers
While if give as input the name of the band for example "Red Hot Chili Peppers", 
the output will be: 
 

    The bassist of Red Hot Chili Peppers is Flea


Instead, for more complicated queries, we can recall some optional arguments.

Here are the optional arguments we decide to implemet in our project:

 - **Add a new bassist (-a)**
 
This argument allows to insert a new bassist to the database. The `-a` activates the `add_element` function which first checks if the bassist already exists in our database and then generate a sequence of questions to insert all the necessary data.

Firstly, we have to wrote in the terminal the name of the artsit we want to add : 

    python main.py "Keith Richards" -a

As the bassist we have insert as input is not present, we will have as output:

    Is he/she a bassist or is it the name of a band (a or b) -> a
    Now enter the full name of the bassist -> Keith Richards
    Now enter the name of the band of the bassist-> The Rolling Stones
    Now enter the music genre of the bassist-> Rock
    Now enter the nationality of the bassist-> British
    Now enter the life period of the bassist->1943-now
    Now enter 'has' or 'has not' depending on whether the bassist had a stage name or not ->has not
    Now enter 'only' or 'never' or 'sometimes' depending on whether the bassist was only, sometimes or never a solist-> sometimes
    Now enter the time period during which the bassist was most famous or successful->80
    Now enter the link to the wikipedia page of the bassist->https://it.wikipedia.org/wiki/Keith_Richards
    Thank you for your contribution!

 - **Find manually if the bassist/band is present in the database (-d)**
 
After being called, the argument `-d` allows to get the database relation between all bassists and bands as follows:

    python main.py "Keith Richards" -d

The output that we optain is the following:

    Now you can see by yourself if the bassist and his/her band are present in our database!
    0                        Flea : Red Hot Chili Peppers
    1                                    Geddy Lee : Rush
    2                               Les Claypool : Primus
    3                      John Paul Jones : Led Zeppelin
    4                                 John Deacon : Queen
    5                           Roger Waters : Pink Floyd
    6                           Tony Levin : King Crimson
    7                         Leland Sklar : Phil Collins
    8                          John Myung : Dream Theater
    9                            John Entwistle : The Who
    10                           Cliff Burton : Metallica
    11                                 Chris Squire : Yes
    12                       Faso : Elio e le Storie Tese
    13                   Thundercat : Suicidal Tendencies
    14                       Duff McKagan : Guns n' Roses
    15                                  Kim Deal : Pixies
    16                          Peter Hook : Joy division
    17    Esperanza Spalding : She was not part of a band
    18               Joseph Makwela : Makgona Tshole Band
    19                              Mike Watt : Minuteman
    20                             George Porter : Meters
    21                        Bill Black : Blue Moon Boys
    22                           Kim Gordon : Sonic youth
    23                              Saturnino : Jovanotti
    24                                Pino Palladio : Who
    25                         John McVie : Fleetwood Mac
    26                        Luis Johnson : Quincy Jones
    27                        Lemmy kilmister : Motšrhead
    28                             Bernard Edwards : Chic
    29             David Hood : He was not part of a band
    30             Bill Wyman : He was not part of a band
    31                 Stanlay Clarke : Return to forever
    32                           Paul McCartney : Beatles
    33                     Victoria De Angelis : Maneskin
    
It's possible to see  bassist and band separatly with the following commands:

-   `python main.py "Queen" -b`  which allows to see the entire list of bands only 
-   `python main.py "Flea" -bas`, to have access to the entire list of bassists only.

• **Print a bio of the bassist (-bio)**

The `return_biography` function can be used to explain the bassist's life in a more understandable and complete way. The code is structured to compile together with the name and  band some details that can be found in the columns of the dataset, and formulates a short biography of the artist.

The function first checks if the input we inserted is present in the database; if not the system will warn and invite you to check if you wrote it correctly.

It's also possible to look at the complete biography using the link from Wikipedia, that will be printed at the end of the output, so that the user can get a complete overview of the artist he/she is interested in.

To use the function the user should recall the optional argument -bio:

    python main.py "Flea" -bio

Thus, the output will be:

    Flea is a/an Australian bassist who lived in these years: 1962-now
    The artist played in Red Hot Chili Peppers  and he/she was most famous 
    in the 90 s. He/She belongs tothe genre of Punk He/She Never played as a 
    soloist, and He/She Has a stage name. Here you can find the web link
    to see the complete biography:  
    https://en.wikipedia.org/wiki/Flea_(musician)

• **Compare different bassists (-s)**

The similarities function allows the user to make some comparisons between the bassist of interest and other bassists in the database. We decide to check the similarities only between 3 columns "Nationality", "Genre" and "Period" as criteria for comparison.

In order to use it the user should recall the optional argument  `-s`  in the following way:

    python main.py "Flea" -s
 
After having inserted the input, the user can choose between different options, according to his/her preference to visualize similarities between bassists based on:

-   Nationality (`nat`),
-   Genre (`gen`),
-   Period (`per`).

Here an example:

    Do you want to see the similarities according to nationality, 
    genre or period of activities? (nat, gen, per) ->

 1. **NATIONALITY** (`nat`)
 
 After you insert `nat` the output will be similar as the following:

    Sorry, there are not Australian bassists

 2. **GENRE** (`gen`)
 
 After you insert `gen` the output will be similar as the following:

    Bassists belonging to Punk genre are the following: 
    Name
    0 Flea
    13  Thundercat
    14  Duff McKagan
    16  Peter Hook

 3. **PERIOD** ( `per`)

While conserning the period a question will be asked, which is if we want to search artist that have been famous on the same period (==), before (<) or after (>) the one of the bassists we are interested of

For example:

    Do you want to search for period that was after (>), before (<) or
    the same (==) period you provided as input? >
    The bassists that were famous after than 90s are the following: 
    Name  Period
    13 Thundercat  2000
    15 Kim Deal  2000
    17 Esperanza Spalding  2000
    23  Saturnino  2000
    33  Victoria De Angelis  2018

 - **Asking for help (-h)**

The last optional argument is `-h`, that gives the user some help about the functioning and the rules of the code. The output in this case will be:

    usage: main.py [-h] [-a | -d | -bio | -b | -bas | -s] name
    This program will check if the name you put is inside our database of 
    bassists and the band in which they play. If the names have more than 
    one space, wrap them around quotes ("").
    positional arguments:
    name  input the name of a known bassist or band
    optional arguments:
    -h, --help  show this help message and exit
    -a, --add add a new bassist or band
    -d, --database  show bassist and relative band
    -bio, --biography entire biography of the bassist
    -b, --bands show the list of bands
    -bas, --bassist show the list of bassists
    -s, --similarities  show similar bassists by nat/gen/per

We can see that this function, make you the list of optional arguments that you can use, and the positional arguments which are needed, and give also a small explaination of the program,  and underline that you have to put the name of the bassists or the band name around quotes.

# Contributing 🤝

  
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please contact us if you wish to implement significant changes and test them before pulling.

# License 📄
  
GNU License

# Authors 👭🏼👩🏻‍🤝‍👩🏼

 - Sofia Favaro 
 - Eleonora Montello
 - Martina Cassin
 - Chiara Govoni
