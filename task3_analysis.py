import pandas as pd
import numpy as np

# load cleaned data from task 2
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print("Loaded data:", df.shape)


# ----------- BASIC INFO -----------

print("\nFirst 5 rows:")
print(df.head())

# average values (using pandas here)
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score   :", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))


# ----------- NUMPY ANALYSIS -----------

print("\n--- NumPy Stats ---")

scores = df["score"].values  # convert to numpy array

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

print("Mean score   :", int(mean_score))
print("Median score :", int(median_score))
print("Std deviation:", int(std_score))

print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))


# which category has most stories
top_cat = df["category"].value_counts().idxmax()
count_cat = df["category"].value_counts().max()

print("\nMost stories in:", top_cat, f"({count_cat} stories)")


# most commented story
max_comments = df["num_comments"].max()

row = df[df["num_comments"] == max_comments]

print("\nMost commented story:")
print(row["title"].values[0], "-", max_comments, "comments")


# ----------- NEW COLUMNS -----------

# engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# popular if score above average
df["is_popular"] = df["score"] > avg_score


# ----------- SAVE FILE -----------

output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

print("\nSaved to", output_file)
