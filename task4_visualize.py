import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_posts.csv")

# top subreddits
subs = df["subreddit"].value_counts().head(5)

plt.figure()
subs.plot(kind="bar")
plt.title("Top Subreddits")
plt.xlabel("Subreddit")
plt.ylabel("Posts")
plt.show()

# score distribution
plt.figure()
plt.hist(df["score"], bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Count")
plt.show()
