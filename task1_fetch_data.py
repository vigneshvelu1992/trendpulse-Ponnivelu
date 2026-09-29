
import requests
import json
import time

# Hacker News Top Stories API
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Call the API
response = requests.get(top_stories_url)

print("Status Code:", response.status_code)

if response.status_code == 200:

    story_ids = response.json()

    print("Total stories available:", len(story_ids))
    print("First 10 story IDs:", story_ids[:10])

    # Fetch details for the first 30 stories
    stories = []

    for story_id in story_ids[:30]:

        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

        story_response = requests.get(story_url)

        if story_response.status_code == 200:

            story = story_response.json()

            if story:
                stories.append(story)

        # Small delay between API requests
        time.sleep(0.1)

    # Save complete story data
    with open("hackernews_raw.json", "w") as file:
        json.dump(stories, file, indent=4)

    print("Stories fetched:", len(stories))
    print("Data saved successfully to hackernews_raw.json")

else:
    print("API request failed")
