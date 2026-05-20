import streamlit as st
import pandas as pd
import time


st.set_page_config(
    page_title="Campaigns",  # the page title shown in the browser tab
    page_icon="🛫",  # the page favicon shown in the browser tab
    layout="wide",  # page layout : use the entire screen
    initial_sidebar_state="expanded" # sidebar already expanded
)

st.title("Campaigns")


# campaign main tableeee
# name
# advertiser
# score 
# Status (on track, under pacing, over pacing)
  
st.subheader("Active Campaigns")
all_camp = pd.DataFrame(
    [
        {"Name": "IffyCoffee Summer Launch", 
         "Advertiser": "IffyCoffee", "Score": 5, 
         "Status": 'On-Track', "Zone(s) Assigned": "Movies, TV",},
 
    ]
)
st.dataframe(
    all_camp,
    key="data",
    on_select="rerun",
    #selection_mode=["multi-row"],
)

st.subheader("Flagged Campaigns 🚩")
# campaigns flagged
# campaign name
# prioroity score
# predicted delivery
# severity (CRITICAL)

flag_camp = pd.DataFrame(
    [
        {"Name": "Never-Ending Pasta", 
         "Priority Score": "Olive Garden", "Zone(s) Assigned": "TV", "Pacing Status": 'Under-Pacing', 
         "Severity": 'CRITICAL'},
 
    ]
)

st.dataframe(
    flag_camp,
    key="dataa",
    on_select="rerun",
    #selection_mode=["multi-row"],
)



with st.sidebar:
    #st.sidebar.image(image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5NVbU9neMehpoxRiJVTCUkvayZ0LNukE39Q&s")
    st.sidebar.title('OneMedia3')
    st.page_link("pages/dashboard.py", label="Dashboard")
    st.page_link("pages/campaigns.py", label="Campaigns")
    st.page_link("login.py", label="Return to Login")