import pandas as pd


df = pd.read_csv("Tracker.csv",parse_dates=['DateTime'],date_format="%m/%d/%Y %I:%M:%S %p")
# Returns a DataFrame
df["Date"] = df["DateTime"].dt.date
daily = df.groupby("Date")["Mood"].mean()
print(daily)