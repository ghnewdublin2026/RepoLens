import streamlit as st
from github_client import GitHubService
import ui_components as ui

st.set_page_config(page_title="GitHub Nexus", layout="wide")

token = ui.render_sidebar()

if token:
    # Initialize Service
    if "gh_service" not in st.session_state:
        st.session_state.gh_service = GitHubService(token)
    
    gh = st.session_state.gh_service

    st.title("🚀 GitHub Dashboard")
    
    tab1, tab2 = st.tabs(["Repositories", "Pull Requests"])

    with tab1:
        repos = gh.get_repositories()
        selected_repo = st.selectbox("Select a Repository", [r.full_name for r in repos])
        
    with tab2:
        if selected_repo:
            prs = gh.get_pull_requests(selected_repo)
            for pr in prs:
                ui.display_pr_card(pr)
else:
    st.warning("Please enter your GitHub Personal Access Token in the sidebar to begin.")
