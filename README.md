

# 🧠 Mental State Tracker (MST)

A fast, zero-bloat daily logging dashboard built from scratch to track mental state, sleep quality, and stray thoughts.

## What It Does

* **Daily Metrics:** Slider inputs (`0–10`) for logging **Mood**, **Sleep**, and **Euphoria**.


* **Brain Dump:** Quick text input to offload thoughts and clear your head, displaying the 3 most recent entries.


* **Rolling Analytics:** Sidebar metrics that automatically group entries by date and calculate true **7-day rolling averages** using Pandas.


* **Local-First Storage:** Appends every log directly to a local `Tracker.csv` file with full 12-hour timestamps.



##  Run Locally

Run these commands in your terminal to launch the tracker offline on your machine:

```bash
git clone [https://github.com/Glory-bot-art/Rebuiding-Mst.git](https://github.com/Glory-bot-art/Rebuiding-Mst.git)
cd Rebuiding-Mst
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py

```

Once running, open `http://localhost:8501` in your browser. All entries are written directly to `Tracker.csv` in the project root.

---

Save the file in VS Code, then run `git add README.md`, `git commit -m "fix readme formatting"`, and `git push` in your terminal so you don't run into that remote sync error again.
