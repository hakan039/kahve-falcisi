from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Gizlilik Politikası", page_icon="🔒", layout="centered")

privacy_policy = (Path(__file__).resolve().parent.parent / "privacy.html").read_text(
    encoding="utf-8"
)
# Keep enough room for the full policy while allowing the embedded page to scroll.
PRIVACY_PAGE_HEIGHT = 1200
components.html(privacy_policy, height=PRIVACY_PAGE_HEIGHT, scrolling=True)
