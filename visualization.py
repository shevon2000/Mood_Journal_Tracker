import matplotlib.pyplot as plt

def visualize_mood_trends(mood_data, dates):
    if mood_data:
        # Plot the mood trends
        plt.figure(figsize=(10, 5))
        plt.plot(dates, mood_data, marker='o', linestyle='-', color='b')
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Mood Rating')
        plt.title('Mood Trends Over Time')
        plt.tight_layout()
        plt.show()
    else:
        raise ValueError("No mood data found to visualize.")
