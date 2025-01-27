import os
from datetime import datetime
from textblob import TextBlob

if not os.path.exists("diary_entries"):
    os.makedirs("diary_entries")

def record_entry(mood, thoughts):
    date = datetime.now().strftime("%Y-%m-%d")

    if not thoughts.strip():
        raise ValueError("Please enter your thoughts.")

    # Save the entry to a file
    with open(f"diary_entries/{date}.txt", "w") as file:
        file.write(f"Date: {date}\n")
        file.write(f"Mood: {mood}/10\n")
        file.write(f"Thoughts:\n{thoughts}\n")

    # Analyze sentiment
    sentiment = analyze_sentiment(thoughts)

    return sentiment

def analyze_sentiment(thoughts):
    blob = TextBlob(thoughts)
    sentiment = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def collect_mood_data():
    mood_data = []
    dates = []

    for filename in os.listdir("diary_entries"):
        if filename.endswith(".txt"):
            with open(f"diary_entries/{filename}", "r") as file:
                lines = file.readlines()
                mood_line = [line for line in lines if line.startswith("Mood")]
                if mood_line:
                    # Extract mood rating from the "Mood" line
                    mood_rating_str = mood_line[0].split(":")[1].strip()  # Strip spaces
                    mood_rating = int(mood_rating_str.split("/")[0].strip())  # Get the integer part before "/10"
                    date = filename.replace(".txt", "")
                    mood_data.append(mood_rating)
                    dates.append(date)

    return mood_data, dates
