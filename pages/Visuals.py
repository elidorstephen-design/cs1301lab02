# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json

with open("data.json") as f:
    data = json.load(f)

df = pd.DataFrame(data["data_points"])
st.dataframe(df)

st.subheader("Hours Per Week by Genre")
st.bar_chart(df, x="Genre", y="Hours Per Week")
st.caption("Here is how many hours per week I listen to each genre. I wonder how closely my Spotify Wrapped will match with this!")

st.subheader("Hours vs. Rating by Genre")

if "min_hours" not in st.session_state:
    st.session_state.min_hours = 0

st.slider("Show the genres that have at least this many hours per week",
          min_value=0, max_value=13, key="min_hours")

filtered = df[df["Hours Per Week"] >= st.session_state.min_hours]

chart = alt.Chart(filtered).mark_circle(size=200).encode(
    x=alt.X("Hours Per Week", title="Hours Listened Per Week"),
    y=alt.Y("Rating", title="Rating (out of 10)"),
    tooltip=["Genre", "Hours Per Week", "Rating"]
).properties(title="Hours Listened vs. Rating by Genre")

st.altair_chart(chart, use_container_width=True)

mean_now = filtered["Hours Per Week"].mean()
median_now = filtered["Hours Per Week"].median()

if "prev_mean" not in st.session_state:
    st.session_state.prev_mean = mean_now
    st.session_state.prev_median = median_now

col1, col2 = st.columns(2)
col1.metric("Mean hours/week",
            f"{mean_now:.2f}",
            delta=round(mean_now - st.session_state.prev_mean, 2))
col2.metric("Median hours/week",
            f"{median_now:.2f}",
            delta=round(median_now - st.session_state.prev_median, 2))

st.session_state.prev_mean = mean_now
st.session_state.prev_median = median_now

# PART 2: GRAPHS FROM data.csv
st.header("Survey Results")
survey_df = pd.read_csv("data.csv")
st.dataframe(survey_df)


static_chart = alt.Chart(survey_df).mark_bar().encode(
    x=alt.X("Platform:N", title="Platform"),
    y=alt.Y("count()", title="Number of Responses"),
    tooltip=["Platform", "count()"]
).properties(title="Responses by Platform")

st.altair_chart(static_chart, use_container_width=True)
st.caption("Looks like most people I surveyed are streaming on Spotify, with everyone else spread across the other apps")

st.subheader("Listening Hours by Platform")

# 1. Session state for the dropdown
if "platform_choice" not in st.session_state:
    st.session_state.platform_choice = "Spotify"

# 2. The widget (key ties it to session state)
st.selectbox("Choose a platform:",
             sorted(survey_df["Platform"].unique()),
             key="platform_choice")

# 3. Filter the data
platform_df = survey_df[survey_df["Platform"] == st.session_state.platform_choice]

# 4. Chart: hours per day for each response on that platform
st.line_chart(platform_df, x="Genre", y="Hours Per Day")

# 5. Extra credit metrics
mean_now = platform_df["Hours Per Day"].mean()
median_now = platform_df["Hours Per Day"].median()

if "prev_mean_2" not in st.session_state:
    st.session_state.prev_mean_2 = mean_now
    st.session_state.prev_median_2 = median_now

c1, c2 = st.columns(2)
c1.metric("Mean hours/day", f"{mean_now:.2f}",
          delta=round(mean_now - st.session_state.prev_mean_2, 2))
c2.metric("Median hours/day", f"{median_now:.2f}",
          delta=round(median_now - st.session_state.prev_median_2, 2))

st.session_state.prev_mean_2 = mean_now
st.session_state.prev_median_2 = median_now
