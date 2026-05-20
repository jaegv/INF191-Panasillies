# log in page for demo
# for demo purposes, it will not be functional, it'll just work with anything

import streamlit as st

def login_page():
    st.title("Login to Panasonic OneMedia Dashboard")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        st.success("Logged in successfully!")
        st.switch_page("pages/dashboard.py")



if __name__ == "__main__":
    login_page()