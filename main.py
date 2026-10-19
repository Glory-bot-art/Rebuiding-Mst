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

#fixing date
df = pd.read_csv("Tracker.csv",parse_dates=['DateTime'],date_format="%m/%d/%Y %I:%M:%S %p")
df["Date"] = df["DateTime"].dt.date

#writing 7 day average with pandas
Average_Mood=df.groupby("Date")["Mood"].tail(7).mean().round(2)
Average_Sleep=df.groupby("Date")["Sleep"].tail(7).mean().round(2)
Average_Euphoria=df.groupby("Date")["Euphoria"].tail(7).mean().round(2)

#displaying it in sidebar with streamlit
with st.sidebar:
    st.metric(label="Average Mood",value=f"{Average_Mood}")
    st.divider()

    st.metric(label="Average Sleep",value=f"{Average_Sleep}")
    st.divider()

    st.metric(label="Average Euphoria",value=f"{Average_Euphoria}")