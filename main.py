import streamlit as st


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

#what happen after submit 
if st.button("Submit"):
    st.balloons()
    with open ("tracker.csv","a") as file:
        file.write(f"{Mood},{Sleep},{Anger_Burst},{Frustrated}\n")



