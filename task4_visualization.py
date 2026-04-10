import pandas as pd
import matplotlib.pyplot as plt
import os

# load analysed data
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")


# ------------------ CHART 1 ------------------
# top 10 stories by score

top10 = df.sort_values(by="score", ascending=False).head(10)

# shorten long titles (just to fit nicely)
titles = []
for t in top10["title"]:
    if len(t) > 50:
        titles.append(t[:50] + "...")
    else:
        titles.append(t)

plt.figure()
plt.barh(titles, top10["score"])
plt.xlabel("Score")
plt.ylabel("Story")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # highest at top

plt.savefig("outputs/chart1_top_stories.png")
plt.show()


# ------------------ CHART 2 ------------------
# stories per category

counts = df["category"].value_counts()

plt.figure()
counts.plot(kind="bar")
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.savefig("outputs/chart2_categories.png")
plt.show()


# ------------------ CHART 3 ------------------
# score vs comments scatter

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.show()


# ------------------ DASHBOARD ------------------
# combine all charts

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# chart 1 again
axes[0].barh(titles, top10["score"])
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# chart 2 again
axes[1].bar(counts.index, counts.values)
axes[1].set_title("Categories")

# chart 3 again
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.show()


print("charts saved in outputs folder")
