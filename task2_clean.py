import pandas as pd

df = pd.read_json("posts.json")

# removing duplicates if any
df = df.drop_duplicates()

# removing rows with missing values
df = df.dropna()

# filtering small posts (optional but useful)
df = df[df["score"] > 50]

df.to_csv("clean_posts.csv", index=False)

print("clean file saved")
