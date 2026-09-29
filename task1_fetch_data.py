
import requests
import json

# Hacker News Top Stories API
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Call the API
response = requests.get(url)

print("Status Code:", response.status_code)

# Check whether API request was successful
if response.status_code == 200:

    story_ids = response.json()

    print("Total stories:", len(story_ids))
    print("First 10 story IDs:", story_ids[:10])

    # Save raw data
    with open("hackernews_raw.json", "w") as file:
        json.dump(story_ids, file, indent=4)

    print("Data saved successfully to hackernews_raw.json")

else:
    print("API request failed")
