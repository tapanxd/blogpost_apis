# blogpost_apis
api created for a blogpost app

In this repo, I've tried to create 4 different APIs using Flask in Python
1. Will convert the .json files into sql tables in a database
2. Will Sort the Authors on the basis of number of likes, comments and posts
3. Will (i)Sort the Post Titles on the basis of number of likes and comments
        (ii)Filter the Post Titles according to Time
4. Will create bar charts for each individual post:
    Time v number of Likes
    Time v number of Comments --incomplete

BEFORE RUNNING ANY OTHER PYTHON FILE, MAKE SURE YOU HAVE RUN THE app.py THAT'LL CREATE THE DATABASE FOR THE GIVEN .json FILES

ERROR IN FILE:
in app4.py on line 32, there's an internal error, 'TypeError: can only concatenate str (not "int") to str', although the variable date_two is of type string 
