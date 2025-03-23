import streamlit as st  
import pandas as pd 
import datetime 
import csv  
import os  

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        data = pd.read_csv(MOOD_FILE)
        if "Date" not in data.columns or "Mood" not in data.columns:
            return pd.DataFrame(columns=["Date", "Mood"])
        return data
    except Exception as e:
        st.error(f"Error loading mood data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        if os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])  
        writer.writerow([date, mood])

st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data = data.dropna(subset=["Date"]) 
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)

st.write("Build with ❤️ by [Asiya Khan](https://github.com/asiyakhan990)")