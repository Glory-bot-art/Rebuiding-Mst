import streamlit as st
from datetime import datetime
import os
import csv

now = datetime.now()
formatted_12hr = now.strftime("%m/%d/%Y %I:%M:%S %p")
#Main UI
st.header("Mental State Tracker")
st.divider()
Mood =st.slider("Mood" ,0,10,5)
st.divider()
Sleep=st.slider("Sleep",0,10,5)
st.divider()
Anger_Burst=st.slider("Anger Burst?",0,10,5)
st.divider()
Frustrated= st.slider("got Frustrated?",0,10,5)

#defining csv
file_name = "Tracker.csv"
header = ['DateTime','Mood','Sleep',"Anger_Burst","Frustrated"]
result = ", ".join(header)
#what happen after submit 
if st.button("submit"):
    st.balloons()
    if not os.path.exists(file_name):
        with open (file_name,'w')as file:
            file.write('DateTime','Mood','Sleep',"Anger_Burst","Frustrated")
            with open (file_name,"a"):
                file.write(f"{now},{mood}")
else:
     if os.path.exists(file_name):
        with open (file_name,"a",newline="")as file:
            file.write('DateTime','Mood','Sleep',"Anger_Burst","Frustrated")
            with open (file_name,"a")as file:
                file.write(f'{now},{Mood},{Sleep},{Anger_Burst},{Frustrated}\n')