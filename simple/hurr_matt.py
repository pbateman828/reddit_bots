#! /usr/bin/python3 
#looks at the hurricane matthews subreddit and gathers information 
#about South Carolina 

#import time 
import praw 

r = praw.Reddit('South Carolina Hurricane Matthew info gather /u/-username-') 

r.login('-username-', '-password-') 

print('Logged In') 

sub_collection = [] 

matthew_file = open('matthew_sc.txt', 'a') 

sc_words = ['south carolina', 'charleston', 'myrtle beach', 'palmetto'] 

sub_count = 0 

for i in range(1): 
    subreddit = r.get_subreddit('hurricanematthew') 
    for submission in subreddit.get_hot(limit=100): 
        subpost_text = submission.selftext.lower() 
        has_sc = any(string in subpost_text for string in sc_words) 

        if submission.id not in sub_collection and has_sc: 
            sub_count += 1 
            msg = '[%s](Link = %s)(Submission id = %s)(Title = %s)' % (sub_count, submission.short_link, submission.id, submission.title)  
            sub_collection.append(msg) 
            print('Found one') 
        else: 
            pass 

matthew_file.write('Link, submission ids and title' + '\n') 

for write_collection in sub_collection: 
    matthew_file.write(write_collection + '\n') 

matthew_file.write('**' * 40) 

print('\n'.join(sub_collection)) 

matthew_file.close() 
 
 
