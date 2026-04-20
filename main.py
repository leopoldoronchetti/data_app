import streamlit as st
from apps.app_finance import app_finance
from components.login import login_page

if __name__ == "__main__":

    st.set_page_config(layout="wide")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        login_page()
    elif "logged_in" in st.session_state:
        app_finance()



