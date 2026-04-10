import requests
import json
import time
import os
from datetime import datetime

# HackerNews API links
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {
    "User-Agent": "TrendPulse/1.0"
}

# categories with keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

all_data = []

try:
    res = requests.get(top_url, headers=headers)
    story_ids = res.json()
except:
    print("error fetching top stories")
    story_ids = []

# take first 500
story_ids = story_ids[:500]

# function to find category
def get_category(title):
    title = title.lower()
    for cat, words in categories.items():
        for w in words:
            if w in title:
                return cat
    return None


# loop category by category
for cat in categories:
    count = 0

    for sid in story_ids:
        if count >= 25:
            break

        try:
            res = requests.get(item_url.format(sid), headers=headers)
            data = res.json()
        except:
            print("failed to fetch story", sid)
            continue

        # skip if no title
        if not data or "title" not in data:
            continue

        title = data["title"]

        assigned = get_category(title)

        # only take if matches current category
        if assigned == cat:
            post = {
                "post_id": data.get("id"),
                "title": title,
                "category": assigned,
                "score": data.get("score", 0),
                "num_comments": data.get("descendants", 0),
                "author": data.get("by"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_data.append(post)
            count += 1

    print(f"{cat} collected:", count)

    # sleep after each category (important)
    time.sleep(2)


# create folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

# filename with date
date_str = datetime.now().strftime("%Y%m%d")
file_name = f"data/trends_{date_str}.json"

# save file
with open(file_name, "w") as f:
    json.dump(all_data, f, indent=2)

print("\nCollected", len(all_data), "stories.")
print("Saved to", file_name)
