
import json
import pandas as pd

with open("hackernews_raw.json", "r") as file:
    stories = json.load(file)
    df = pd.DataFrame(stories)

print(df.head())

df = df[
    ["id", "title", "score", "descendants", "by", "time", "url"]
]

df = df.rename(
    columns={
        "descendants": "comments"
    }
)

df["url"] = df["url"].fillna("No URL")
df["comments"] = df["comments"].fillna(0)
df["score"] = df["score"].fillna(0)

df = df.drop_duplicates(subset="id")

df["engagement"] = df["score"] + df["comments"]

df.to_csv("hackernews_clean.csv", index=False)
