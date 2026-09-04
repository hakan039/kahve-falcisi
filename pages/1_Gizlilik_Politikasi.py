from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Gizlilik Politikası", page_icon="🔒", layout="centered")

privacy_policy = (Path(__file__).resolve().parent.parent / "privacy.html").read_text(
    encoding="utf-8"
)
privacy_page_height = max(600, len(privacy_policy.splitlines()) * 30)
components.html(privacy_policy, height=privacy_page_height, scrolling=True)
