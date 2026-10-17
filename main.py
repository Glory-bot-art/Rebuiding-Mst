import streamlit as st
from datetime import datetime
import os
import pandas as pd

now = datetime.now()
formatted_12hr = now.strftime("%m/%d/%Y %I:%M:%S %p")
#Main UI
Mood =st.slider("Mood" ,0,10,5)
st.divider()
Sleep=st.slider("Sleep",0,10,5)
st.divider()
Euphoria=st.slider("Euphoria",0,10,5)
st.divider()
Brain_dump = st.text_input(
    label= "**Brain_dump**",
    placeholder="Dump any worries,grief or gust thoughts"
)

#defining csv
file_name = "Tracker.csv"
header = ['DateTime','Mood','Sleep','Euphoria','Brain_dump']
result = ",".join(header)
stats = (f"{formatted_12hr},{Mood},{Sleep},{Euphoria},{Brain_dump}\n")

#what happen after submit 
if st.button("submit"):
    if not os.path.exists(file_name):
        with open (file_name,'w',newline="")as file:
            file.write(f"{result}\n{stats}")
    else:
        with open (file_name,"a",newline="")as file:
            file.write(stats)
            st.balloons()


#Analysing things with pandas

df = pd.read_csv("Tracker.csv",parse_dates=['DateTime'],date_format="%m/%d/%Y %I:%M:%S %p")
# Returns a DataFrame
df["Date"] = df["DateTime"].dt.date


Average_Mood=df.groupby("Date")["Mood"].mean()

