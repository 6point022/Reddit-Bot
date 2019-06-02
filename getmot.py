import praw
import config
import os
import time
from random_quote import get_random_quote
from langdetect import detect


def bot_login():
	r = reddit = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = 'GetMotivated Bot v0.1')

	return r

def run_bot(r, comments_replied_to):
	for comment in r.subreddit('all').comments(limit = 1000):
		# print(comment.body.lower())
		if '!motivateme' in comment.body.lower() and comment.id not in comments_replied_to:
			print('Replying to comment')

			while True:
				final_comment = get_random_quote()
				if detect(final_comment) == 'en':
					break
				else:
					print(final_comment, detect(final_comment))

			comment.reply(final_comment)
			comments_replied_to.append(comment.id)

			with open('saved_comments.txt', 'a') as f:
				f.write(comment.id + '\n')

def get_saved_comments():
	if not os.path.isfile('saved_comments.txt'):
		comments_replied_to = []
	else:		
		with open('saved_comments.txt', 'r') as f:
			file_data = f.read()
			comments_replied_to = file_data.split('\n')

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
# print(comments_replied_to)
run_bot(r, comments_replied_to)

while True:
	try:
		run_bot(r, comments_replied_to)
		print("sleeping for 2 sec")
		time.sleep(2)
	except:
		continue