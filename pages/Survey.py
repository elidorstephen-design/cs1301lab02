# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to add your data to the dataset.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    genre_input = st.text_input("What's your favorite music genre?")
    hours_input = st.slider("About how many hours a day do you listen to music?", 0, 12, 2)
    platform_input = st.selectbox("How do you mostly listen?",
                                  ["Spotify", "Apple Music", "YouTube", "Radio", "Other"])

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        if genre_input.strip() == "":
            st.error("Please enter a genre.")
        else:
            new_row = pd.DataFrame({
                "Genre": [genre_input.strip().title()],
                "Hours Per Day": [hours_input],
                "Platform": [platform_input]
            })
            file_has_data = os.path.exists("data.csv") and os.path.getsize("data.csv") > 0
            new_row.to_csv("data.csv", mode="a", header=not file_has_data, index=False)
            st.success("Your data has been submitted!")
            st.write(f"You entered: **Genre:** {genre_input}, **Hours Per Day:** {hours_input}, **Platform:** {platform_input}")        



# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
