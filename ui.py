import tkinter as tk
from tkinter import messagebox
from mood_tracker import record_entry, collect_mood_data
from visualization import visualize_mood_trends

def setup_ui():
    window = tk.Tk()
    window.title("Mood Journal Tracker")
    window.configure(bg="#f2f2f7")

    tk.Label(window, text="Rate your mood from 1 to 10:", bg="#f2f2f2", font=("Helvetica", 12)).pack(pady=5)
    mood_var = tk.IntVar()
    mood_scale = tk.Scale(window, from_=1, to=10, orient="horizontal", variable=mood_var, bg="#e6e6e6", sliderlength=20)
    mood_scale.pack(pady=5)

    tk.Label(window, text="Write your thoughts (press Enter on an empty line to finish):", bg="#f2f2f2", font=("Helvetica", 12)).pack(pady=5)
    thoughts_text = tk.Text(window, height=8, width=50, bg="#333333", fg="white", font=("Helvetica", 12), padx=10, pady=10)
    thoughts_text.pack(pady=5)

    sentiment_label = tk.Label(window, text="Sentiment: ", bg="#f2f2f2", font=("Helvetica", 12))
    sentiment_label.pack(pady=5)

    def save_diary_entry():
        mood = mood_var.get()
        thoughts = thoughts_text.get("1.0", "end-1c")

        try:
            sentiment = record_entry(mood, thoughts)
            sentiment_label.config(text=f"Sentiment: {sentiment}")
            messagebox.showinfo("Success", "Your diary entry has been saved.")
        except ValueError as e:
            messagebox.showwarning("Input Error", str(e))

    def show_mood_trends():
        try:
            mood_data, dates = collect_mood_data()
            visualize_mood_trends(mood_data, dates)
        except ValueError as a:
            messagebox.showwarning("Error", str(e))

    record_button = tk.Button(window, text="Save Diary Entry", command=save_diary_entry, bg='#4CAF50', fg="white", font=("Helvetica", 12), width=20)
    record_button.pack(pady=10)

    visualize_button = tk.Button(window, text="Visualize Mood Trends", command=show_mood_trends, bg='#2196F3', fg="white", font=("Helvetica", 12), width=20)
    visualize_button.pack(pady=10)

    exit_button = tk.Button(window, text="Exit", command=window.quit, bg='#f44336', fg="white", font=("Helvetica", 12), width=20)
    exit_button.pack(pady=10)

    footer = tk.Label(window, text="Designed and developed by SH_Coders\n all rights reserved by M.S.H.M.Fernando", fg="gray", font=("Helvetica", 10), bg='#f2f2f2')
    footer.pack(side="bottom", pady=10)

    window.mainloop()


