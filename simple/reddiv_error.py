#! /usr/bin/python3 
#looks at the redditdev subreddit and writes submissions 
#to a text file. Only checks first ten submissions of (hot)redditdev 

#import time  
import praw 

#from pprint import pprint 
 
r = praw.Reddit('PRAW redditdev search /u/-username- v 1.0.') 

r.login('-username-','-password-') 

print('Logged In') 
 
found_subid = [] 

#file that submissions are written to
file_writeto = open('redditsub.txt', 'a')

errors_words = ['praw', 'captcha', 'error', 'trouble'] 


sub_count = 0 #keeps count of how many subs are found

#can change this to a while loop and set a timer.sleep if you want to run this for a while

for i in range(1): 
    subreddit = r.get_subreddit('redditdev') 
    for submission in subreddit.get_hot(limit=10): #limit is how many submissions you want to look at
        op_text = submission.selftext.lower() 
        has_praw = any(string in op_text for string in errors_words) #looks for error related question or praw related question 
        
        
        if submission.id not in found_subid and has_praw: 
            sub_count += 1 
            msg = '[%s](Link = %s)(Submission id = %s)(Title = %s)' % (sub_count, submission.short_link, submission.id, submission.title)  
            found_subid.append(msg) 
            print ('We found one') 
        else: 
            pass

#title
file_writeto.write('Submission ids and URLs' + '\n')

#writes list to file
for i in found_subid: 
    file_writeto.write(i +'\n')  

file_writeto.write('-' * 40)         

print('\n'.join(found_subid))
 

file_writeto.close() 

