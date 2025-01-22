"""Shorturl app"""
import streamlit as st

st.title("Short URL Generator")

# Tabs for different sections
tab1, tab2 = st.tabs(["Shorten URL", "Analytics"])

# Tab 1: Shorten URL
with tab1:
    original_url = st.text_input("Enter the URL to shorten")
    if st.button("Generate Short URL"):
        st.write('Button clicked')

# Tab 2: Analytics
with tab2:
    short_id = st.text_input("Enter the Short ID for analytics")
    if st.button("Get Analytics"):
        st.write('Get Analytics Button clicked')
