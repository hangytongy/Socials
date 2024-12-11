import praw
from datetime import datetime
import pandas as pd
import time
from telegram_push import post_message

# Set up the Reddit API client using your credentials
reddit = praw.Reddit(
    client_id='',          # Your Reddit API client ID
    client_secret='',  # Your Reddit API client secret
    user_agent='myBot/1.0',        # A unique user agent string (e.g. 'myBot/1.0')
)

def get_subreddit(name = 'Pepecryptocurrency'):

    # Define the subreddit name
    subreddit_name = name  # Replace with the desired subreddit

    # Access the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    return subreddit

def get_follower_count(subreddit,name = 'Pepecryptocurrency'):

    subreddit_name = name

    # Get the number of followers (subscribers)
    followers_count = subreddit.subscribers
    message = f"Subreddit '{subreddit_name}' has {followers_count} followers."
    
    return message

def get_latest_posts(subreddit):
    latest = {'date' : [], 'score' : []}

    # Fetch the hot post (this returns posts sorted by hotness, you can specify 'limit')
    latest_posts = subreddit.new(limit=5)  # Get the hottest post

    # Display the hot posts information
    for post in latest_posts:
        #print(f"Title: {post.title}")
        #print(f"Author: {post.author}")
        #print(f"URL: {post.url}")
        #print(f"Score: {post.score}")
        dt_object = datetime.utcfromtimestamp(post.created_utc)
        formatted_dt = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        #print(f"Created: {formatted_dt}")  # Timestamp in UTC
        #print('-' * 40)  # Separator between posts
        
        latest['date'].append(formatted_dt)
        latest['score'].append(post.score)
    
    message = f"Latest Posts\n\n1st : Date = {latest['date'][0]}, score = {latest['score'][0]}\n5th : Date = {latest['date'][-1]}, score = {latest['score'][-1]}"
    return message

def get_hot_posts(subreddit):
    hot = {'date' : [], 'score' : []}

    # Fetch the hot post (this returns posts sorted by hotness, you can specify 'limit')
    hot_posts = subreddit.hot(limit=5)  # Get the hottest post

    # Display the hot posts information
    for post in hot_posts:
        #print(f"Title: {post.title}")
        #print(f"Author: {post.author}")
        #print(f"URL: {post.url}")
        #print(f"Score: {post.score}")
        dt_object = datetime.utcfromtimestamp(post.created_utc)
        formatted_dt = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        #print(f"Created: {formatted_dt}")  # Timestamp in UTC
        #print('-' * 40)  # Separator between posts
        
        hot['date'].append(formatted_dt)
        hot['score'].append(post.score)
        
    #get hot topics latest post and score
    df = pd.DataFrame(hot)

    df_sorted = df.sort_values(by='date', ascending=False)
    message = f"Latest Hot post\n\nDate = {df_sorted.loc[0,'date']}, Score = {df_sorted.loc[0,'score']}"

    return message

names = ['Pepecryptocurrency','dogwifhat']

for name in names:
    subreddit = get_subreddit(name)

    followers = get_follower_count(subreddit,name)
    #print(followers)

    latest = get_latest_posts(subreddit)
    #print(latest)

    hot = get_hot_posts(subreddit)
    #print(hot)

    messages = f"{name}\n\n{followers}\n\n{latest}\n\n{hot}\n"

    print(messages)
    post_message(messages)

    time.sleep(5)

