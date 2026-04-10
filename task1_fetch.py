import requests
import json

url = "https://www.reddit.com/r/popular.json"

headers = {
    "User-Agent": "trendpulse-script"
}

res = requests.get(url, headers=headers)

data = res.json()

all_posts = []

for item in data["data"]["children"]:
    post = item["data"]
    
    post_info = {
        "title": post.get("title"),
        "score": post.get("score"),
        "subreddit": post.get("subreddit"),
        "comments": post.get("num_comments"),
        "link": post.get("url")
    }
    
    all_posts.append(post_info)

with open("posts.json", "w") as f:
    json.dump(all_posts, f, indent=2)

print("done fetching")
