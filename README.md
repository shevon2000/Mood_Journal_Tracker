```markdown
# Mood Tracker

A Python-based mood tracker application with a GUI interface built using Tkinter. The project allows users to log their daily mood, thoughts, and view sentiment analysis and mood trends.

## Features
- **Mood Logging:** Record your daily mood on a scale of 1 to 10.
- **Sentiment Analysis:** Analyze the sentiment of your thoughts (Positive, Negative, Neutral).
- **Visualization:** Visualize your mood trends over time using a graphical chart.
- **User-Friendly Interface:** Simple and clean GUI built with Tkinter.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mood-tracker.git
   cd mood-tracker
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   # Activate the environment
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.7+
- Tkinter (comes with Python by default)
- `matplotlib`
- `textblob`

Install dependencies with:
```bash
pip install matplotlib textblob
```

## Usage
1. Launch the application by running `main.py`.
2. Use the slider to rate your mood and type your thoughts in the text box.
3. Click "Save Diary Entry" to save your mood log.
4. Click "Visualize Mood Trends" to see a graph of your mood over time.

## File Structure
- **main.py**: Entry point for the application.
- **ui.py**: Contains the GUI logic.
- **mood_tracker.py**: Handles mood logging, file saving, and sentiment analysis.
- **visualization.py**: Generates mood trend visualizations.
- **diary_entries/**: Stores user diary entries as text files.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License.

---

Designed and developed by SH_Coders. All rights reserved by M.S.H.M. Fernando.
 
