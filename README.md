# 🚀 RepoLens: Custom GitHub Intelligence Dashboard

A modular Streamlit interface for managing GitHub private/public repositories, tracking Pull Requests, and monitoring Project V2 statuses in one unified view.

## 🏗️ Architecture
This project uses a **modular service-oriented architecture** to ensure scalability and ease of maintenance:

* `app.py`: The main entry point and UI layout controller.
* `github_client.py`: A dedicated service class handling GitHub API/GraphQL interactions.
* `ui_components.py`: Reusable Streamlit widgets and layout fragments.
* `utils.py`: Helper functions for data parsing and date formatting.

## ✨ Features
* **Dual-Scope Visibility:** Seamlessly toggle between public and private repositories.
* **Unified PR Tracker:** View all open Pull Requests across selected repos with status badges.
* **Project V2 Support:** Integration with GitHub Projects (Beta) via GraphQL.
* **Smart Caching:** High-performance data fetching using `st.cache_data` to respect API rate limits.

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/youruser/repolens.git](https://github.com/youruser/repolens.git)
    cd repolens
    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit PyGithub pandas
    ```

3.  **Authentication:**
    * Generate a [GitHub Personal Access Token (PAT)](https://github.com/settings/tokens).
    * Ensure the token has `repo`, `read:org`, and `project` scopes.

4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 🔒 Security Note
This application handles sensitive GitHub PATs. When deploying, ensure you use `st.secrets` or environment variables. Never commit your tokens to version control.

---
*Built with ❤️*
