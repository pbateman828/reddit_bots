#! /usr/bin/python3 
#looks at the redditdev subreddit and writes submissions 
#to a text file 

import time  
import praw 
from pprint import pprint 

r = praw.Reddit('PRAW redditdev search /u/loubloom12 v 1.0.') 

r.login() 

print('Logged In') 
 
found_subid = [] 


file_writeto = open('redditsub.txt', 'a')

errors_words = ['praw', 'captcha', 'error', 'trouble'] 

for i in range(1): 
    subreddit = r.get_subreddit('redditdev') 
    for submission in subreddit.get_hot(limit=10): 
        op_text = submission.selftext.lower() 
        has_praw = any(string in op_text for string in errors_words) 

        if submission.id not in found_subid and has_praw: 
            msg = '[praw error related thread](Link = %s)(Submission id = %s)(Title = %s)' % (submission.short_link, submission.id, submission.title)  
            found_subid.append(msg) 
            print ('We found one') 
        else: 
            pass

file_writeto.write('Submission ids and URLs' + '\n')
for i in found_subid: 
    file_writeto.write(i +'\n')  
         

print('\n'.join(found_subid))

file_writeto.close() 

