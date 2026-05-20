import streamlit as st
import pandas as pd

def run_main():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 30, 18],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    edited_df = st.data_editor(df)

    # add_selectbox = st.sidebar.selectbox(
    #     "How would you like to be contacted?",
    #     ("Email", "Home phone", "Mobile phone")
    # )

if __name__ == "__main__":
    run_main()

# Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

