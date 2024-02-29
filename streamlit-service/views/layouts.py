import streamlit as st
from models import charts
import os


def get_markdown(folder: str, file: str) -> str:
    """Return a markdown file from a specified folder as a string

    Args:
        folder (str): Folder from `_markdown/`
        file (str): File from `_markdown/`

    Returns:
        str: Markdown as string
    """
    md = None
    md_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "_markdown",
        folder,
        f"{file}.md",
    )

    with open(md_path, "r") as f:
        md = f.read()

    return md


class Page:
    def __init__(self, title):
        st.markdown(f"# {title}")


class HomePage(Page):
    def __init__(self, title):
        super().__init__(title)

    def sidebar_content(self):
        st.sidebar.markdown(get_markdown("home", "sidebar1"))

    def main_content(self):
        st.markdown(get_markdown("home", "main1"))


class SecondPage(Page):
    def __init__(self, title):
        super().__init__(title)

    def sidebar_content(self):
        st.sidebar.markdown(get_markdown("page2", "sidebar1"))

    def main_content(self):
        st.markdown(get_markdown("page2", "main1"))
        st.write(charts.module_dataframes["first_table"])
