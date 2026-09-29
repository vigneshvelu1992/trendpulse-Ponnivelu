
import pandas as pd
df = pd.read_csv("hackernews_clean.csv")

#best scoring Story
top_score = df.sort_values(
    by="score",
    ascending=False
).head(10)

print(top_score[["title", "score"]])


#stories with most comments
top_comments = df.sort_values(
    by="comments",
    ascending=False
).head(10)

print(top_comments[["title", "comments"]])


#most engaging story
top_engagement = df.sort_values(
    by="engagement",
    ascending=False
).head(10)

print(top_engagement[["title", "engagement"]])



#Finding Average score
print("Average score:", df["score"].mean())
print("Maximum score:", df["score"].max())
print("Average comments:", df["comments"].mean())
print("Maximum comments:", df["comments"].max())



#Most popular story
most_popular = df.loc[df["score"].idxmax()]

print("Most popular story:")
print(most_popular["title"])
print("Score:", most_popular["score"])
