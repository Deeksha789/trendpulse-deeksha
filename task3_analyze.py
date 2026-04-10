import pandas as pd
import numpy as np

df = pd.read_csv("clean_posts.csv")

# average score
avg = np.mean(df["score"])
print("average score:", avg)

# most common subreddit
top_sub = df["subreddit"].value_counts().idxmax()
print("top subreddit:", top_sub)

# most commented post
max_comments = df["comments"].max()

row = df[df["comments"] == max_comments]

print("\nmost commented post:")
print(row["title"].values[0])
print("comments:", max_comments)
