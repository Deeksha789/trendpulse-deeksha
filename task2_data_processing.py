import pandas as pd
import os

# find json file inside data folder
folder = "data"
files = os.listdir(folder)

json_file = None

for f in files:
    if f.endswith(".json"):
        json_file = os.path.join(folder, f)
        break

# if no file found
if json_file is None:
    print("no json file found in data folder")
    exit()

# load json
df = pd.read_json(json_file)

print("Loaded", len(df), "stories from", json_file)


# ------------------ CLEANING ------------------

# remove duplicates based on post_id
before = len(df)
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates:", len(df))


# remove rows with missing important fields
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))


# fix data types (sometimes they come as float or object)
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# remove low quality posts
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))


# clean title (remove extra spaces)
df["title"] = df["title"].str.strip()


# ------------------ SAVE ------------------

output_file = "data/trends_clean.csv"

df.to_csv(output_file, index=False)

print("\nSaved", len(df), "rows to", output_file)


# ------------------ SUMMARY ------------------

print("\nStories per category:")

counts = df["category"].value_counts()

for cat, count in counts.items():
    print(f"  {cat}  {count}")
