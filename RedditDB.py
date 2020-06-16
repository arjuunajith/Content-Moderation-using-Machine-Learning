import praw
import pandas as pd

reddit=praw.Reddit(client_id='ThExMcDCYM_RCw',client_secret='rBHhVDV4AkGCB2bYkIRp9AiTH9Y',user_agent='MainPro')

posts = []

ml_subreddit = reddit.subreddit('all')

for post in ml_subreddit.hot(limit=10):

    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

print(posts)