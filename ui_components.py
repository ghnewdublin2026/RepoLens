import streamlit as st

def render_sidebar():
    st.sidebar.title("Settings")
    token = st.sidebar.text_input("GitHub PAT", type="password")
    return token

def display_pr_card(pr):
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        col1.markdown(f"**[{pr.title}]({pr.html_url})**")
        col2.info(f"Status: {pr.state.upper()}")
        st.caption(f"Opened by {pr.user.login} on {pr.created_at.date()}")
