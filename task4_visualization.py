import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hackernews_clean.csv")


#Chart 1 -Top Stories by Score
top3 = df.sort_values(
    by="score",
    ascending=False
).head(3)

plt.figure(figsize=(3, 6))

plt.barh(
    top3["title"],
    top3["score"]
)

plt.xlabel("Score")
plt.ylabel("Story")
plt.title("Top 3 Hacker News Stories by Score")

plt.tight_layout()

plt.savefig("top_stories_score.png")

plt.show()


#Chart2 - Score vs Comments
plt.figure(figsize=(8, 6))

plt.scatter(
    df["score"],
    df["comments"]
)

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Hacker News Score vs Comments")

plt.tight_layout()

plt.savefig("score_vs_comments.png")

plt.show()
