import praw
import time
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://stats.nba.com/players/list/')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

print([a.text.lower().strip() for a in soup.select(".players-list__names a")])

# reddit = praw.Reddit(client_id='HHZ5FFVA72bOFA',
# 					 client_secret='d2vtaU2gMLhxZ9x6nfxFtWp-AS0',
# 					 user_agent= 'This is a test bot',
# 					 username='',
# 					 password='')

# subreddit = reddit.subreddit('nba')
# keywords= ['stats']
# sleep_time = None


# for comment in reddit.subreddit('nba').stream.comments(): #Looking for 'stats player name'
# 	for keyword in keywords:
# 			if keyword in comment.body.split():
# 				try:
# 					new_coment = comment.reply('Shhhhh... all you gotta do is trust The Process.')
# 					print(new_coment.body)
# 				except praw.exceptions.APIException as e:
# 					time.sleep(600)

