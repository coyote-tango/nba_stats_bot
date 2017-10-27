import praw
import time

reddit = praw.Reddit(client_id='HHZ5FFVA72bOFA',
					 client_secret='d2vtaU2gMLhxZ9x6nfxFtWp-AS0',
					 user_agent= 'This is a test bot',
					 username='',
					 password='')

subreddit = reddit.subreddit('nba')
keywords= ['stats']
sleep_time = None


for comment in reddit.subreddit('nba').stream.comments(): #Looking for 'stats player name'
	for keyword in keywords:
			if keyword in comment.body.split():
				try:
					new_coment = comment.reply('Shhhhh... all you gotta do is trust The Process.')
					print(new_coment.body)
				except praw.exceptions.APIException as e:
					time.sleep(600)


if __name__ == '__main__':
	main()