import praw
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Connect to Reddit
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def get_user_content(username, limit=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        # Fetch posts
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "url": submission.permalink
            })

        # Fetch comments
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "url": comment.permalink
            })

    except Exception as e:
        print("❌ Error fetching data:", e)

    return posts, comments
