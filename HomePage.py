# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("What's Everyone Listening To? 🎧")

# INTRODUCTORY TEXT
st.write("""
Hello, my name is Stephen Elidor and welcome to my CS 1301 Lab 02 Website! I picked music for this project because it's something I use every day and love.
First I charted my own weekly listening by genre, then I surveyed other people
about their favorite genre, how many hours a day they listen, and which platform they use.

### How to use this app:
- **Survey Page**: Answer three quick questions to add your data to the dataset.
- **Visuals Page**: See my listening habits at the top of the page and the survey results in charts at the bottom.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
