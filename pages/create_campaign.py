import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Create Campaign",  # the page title shown in the browser tab
    page_icon="🛫",  # the page favicon shown in the browser tab
    layout="wide",  # page layout : use the entire screen
    initial_sidebar_state="expanded" 
)

st.title("Create A Campaign")
#
with st.sidebar:
    #st.sidebar.image(image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5NVbU9neMehpoxRiJVTCUkvayZ0LNukE39Q&s")
    st.sidebar.title('OneMedia3')
    st.page_link("pages/dashboard.py", label="Dashboard")
    st.page_link("pages/campaigns.py", label="Campaigns")
    st.page_link("login.py", label="Return to Login")


with st.container(horizontal=False, border=True):
    st.header('Step 1 - Identify Campaign')
    st.text_input("Campaign Name")
    st.text_input("Advertiser Name")
    c_type = st.selectbox("Creative Type", ('Banner', 'Video'))
    st.selectbox("Goal Type", ('Consideration', 'Awareness'))
    st.selectbox("Revenue Type", ('Paid', 'Partner', 'House'))
    st.date_input("Start Date")
    st.date_input("End Date")
    st.number_input("Impressions Goal", value=None)

with st.container(horizontal=False, border=True):
    st.header('Step 2 - Upload Campaign')
    if c_type == 'Video':
        st.file_uploader("Upload Campaign Media", accept_multiple_files=True, type="mp4")
        st.selectbox(
        "Allow Skipping", 
        ('No', 'Yes', 'Yes, after 5 seconds', 'Yes, after 10 seconds')
    )
    else:
        st.file_uploader("Upload Campaign Media", accept_multiple_files=True, type="png")
        st.number_input("Interstitial Duration (in seconds)", 5)
    st.text_input("Creative Size Dimensions")
    #st.text_input("Program Match")
    #st.text_input("Audience Fit")
    #st.text_input("Inventory Status")

with st.container(horizontal=False, border=True):
    st.header('Step 3 - Zone Selection')
    df = pd.DataFrame(
    [
        {"Zone Section": "Movies (new releases, action, comedy, drama, horror, sci-fi, etc., plus every language subtitle/audio variant)", "Program": "Pan Air Seatback", "Rating": 5, "Reccomended": True, "Why Reccomended": "Matches target interest",},
        {"Zone Section": "TV (comedy, drama, documentary, HBO Max, Peacock, Apple TV, etc., plus every language variant)" , "Program": "Pan Air Seatback", "Rating": 4, "Reccomended": True, "Why Reccomended": "Matches target interest",},
        {"Zone Section": "Audio (audiobooks, playlists, podcasts)" , "Program": "Pan Air Seatback", "Rating": 2, "Reccomended": False},
        {"Zone Section": "Games" , "Program": "Pan Air Seatback", "Rating": 1, "Reccomended": False},
        {"Zone Section": "Retail (luggage, tech gadgets, travel accessories)" , "Program": "Pan Air Seatback", "Rating": 1, "Reccomended": False},
 
    ]
)

    st.dataframe(
    df,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row"],
)



with st.container(horizontal=False, border=True):
    st.header('Step 4 - Budget & Cap')
    st.selectbox(
        "Pricing Model", ('CPC', 'CPM', 'Tenancy')
    )
    st.number_input("Pricing Model Cost", value=None)
    st.number_input("Flight Impressions Cap", value=None)
    freq = st.selectbox(
        "Frequency Cap", ('None', 'Yes, 3 per hour', 'Custom')
    )
if freq == 'Custom': 
    with st.container(horizontal=False, border=True):
        st.header('Step 4a - Frequency Cap')
        
        limit = st.number_input("Campaign Limit Amount", value=None, step=1)
        per = st.number_input("Frequency Time", value=None, step=1)
        timez = st.selectbox(
            "Frequency Time Type", ('Hour(s)', 'Day(s)', 'Week(s)', 'Month(s)')
        )
        st.divider()
        st.write("My Campaign will run: ", limit,'times every', per, timez)
        st.divider()
        



if st.button("Submit for Review", type="primary"):
    st.switch_page("pages/dashboard.py")
    