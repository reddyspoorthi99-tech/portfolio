import streamlit as st

# Set page config
st.set_page_config(page_title="Spoorthi Reddy | Portfolio", layout="wide")

# Load your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display HTML inside Streamlit
st.components.v1.html(html_code, height=1000, scrolling=True)
