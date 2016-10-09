#! /usr/bin/python3  
import time 
import praw  
from pprint import pprint 

# r is the description that the reddit API sees. 
#use your own username /u/ 
r = praw.Reddit('PRAW related-question monitor by /u/#yourusername# v 1.1. '
                'Url: https://praw.readthedocs.org/en/latest/'
                'pages/writing_a_bot.html') 

r.login() 

submission = r.get_submission(submission_id = "105aru") 

#vars contains the objects attributes and the values they contain
#compare print statements to https://www.reddit.com/r/learnpython/comments/105aru/newbie_stripping_strings_of_last_character/

pprint(vars(submission)) 

#dir returns the names in the local scope

pprint(dir(submission))


