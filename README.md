
```markdown
# Mental State Tracker (MST)

A minimalist, fast daily logging dashboard built to track mental well-being, sleep quality, and intrusive thoughts without any fluff. Built with Python, Streamlit, and Pandas.

## Features

- **Quick Logging:** Simple slider inputs for daily Mood, Sleep, and Euphoria levels.
- **Brain Dump:** A dedicated text entry for offloading daily worries, grief, or stray thoughts.
- **Automated Analytics:** Automatically calculates and displays 7-day rolling averages for your core metrics to help spot trends.
- **Local Privacy:** Saves all data locally to a `Tracker.csv` file, ensuring complete ownership over your personal entries. 
- **Sidebar Dashboard:** Instant visual feedback on your current weekly metrics.

## Tech Stack

- **Frontend/Backend:** [Streamlit](https://streamlit.io/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **Language:** Python 3.x

## Local Installation & Usage

To run this app on your own machine (recommended for keeping your data saved locally):

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Glory-bot-art/Rebuiding-Mst.git](https://github.com/Glory-bot-art/Rebuiding-Mst.git)
   cd Rebuiding-Mst

```

2. **Set up a virtual environment (optional but recommended):**
```bash
python -m venv .venv
source .venv/bin/activate

```


3. **Install the dependencies:**
```bash
pip install -r requirements.txt

```


4. **Launch the application:**
```bash
streamlit run main.py

```



The app will open automatically in your default web browser at `http://localhost:8501`.

## Data Storage

When you submit an entry, the application automatically generates and appends to a `Tracker.csv` file in the root directory. Do not delete this file if you wish to keep your historical data.

```

```
