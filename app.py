"""Shorturl app"""
import streamlit as st
from src.utils.helpers import generate_short_url
from src.utils.url_validator import is_valid_url

st.title("Short URL Generator")

# # Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Shorten URL", "Short-URL Clicks", "All ShortURLs"])

# Tab 1: Shorten URL
with tab1:
    original_url = st.text_input("Enter the URL to shorten")
    button = st.button('Generate Short URL')
    if original_url:
        if button:
            IS_VALID = is_valid_url(original_url)
            if not IS_VALID:
                st.write('Please enter a Valid URL')
            else:
                # Create a JSON object
                json_data = generate_short_url(
                    original_url=original_url
                )
                # st.write('Button clicked')
                st.write(json_data.get("short_url"))

# Tab 2: Analytics
with tab2:
    short_id = st.text_input("Enter the Short ID for analytics")
    if st.button("Get Analytics"):
        st.write('Get Analytics Button clicked')
