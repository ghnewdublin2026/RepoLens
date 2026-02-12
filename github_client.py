import streamlit as st
from github import Github, Auth

class GitHubService:
    def __init__(self, token):
        self.auth = Auth.Token(token)
        self.client = Github(auth=self.auth)

    @st.cache_data(ttl=600)  # Cache results for 10 minutes
    def get_repositories(_self):
        # Fetching both private and public
        return [repo for repo in _self.client.get_user().get_repos()]

    @st.cache_data(ttl=300)
    def get_pull_requests(_self, repo_name):
        repo = _self.client.get_repo(repo_name)
        return repo.get_pulls(state='open')
