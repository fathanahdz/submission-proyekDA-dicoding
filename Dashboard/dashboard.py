import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_monthly(df): 
    monthly_df = df.groupby(by=['year', 'month'])[['count']].mean().reset_index()
    return monthly_df

def create_hourly(df):
    hourly_rental_df = df.groupby(by=['year', 'hour'])[['count']].mean().reset_index()
    return hourly_rental_df

def create_season(df):
    season_df = df.groupby(by='season')[['count']].sum().reset_index()
    return season_df

def create_weather(df):
    weather_df = df.groupby(by = 'weather')[['count']].sum().reset_index()
    return weather_df

def create_rfm(df):
    rfm_df = df.groupby(by="instant", as_index=False).agg({
    "dateday": "max",        # Mengambil tanggal terakhir penyewaan sepeda dilakukan
    "weekday": "mean",       # Mengambil Hari dengan penyewaan terbanyak
    "count": "max"           # Menghitung jumlah penyewaan yang telah dilakukan
    })

    rfm_df.columns = [
        "weekday", 
        "recent_dateday", 
        "frequency",
        "monetary"
    ]
    
    # menghitung kapan terakhir pelanggan melakukan transaksi (tanggal)
    rfm_df["recent_dateday"] = rfm_df["recent_dateday"].dt.date
    recent_date = df['dateday'].dt.date.max()
    rfm_df["recency"] = rfm_df["recent_dateday"].apply(lambda x: (recent_date - x).days)
    
    rfm_df.drop("recent_dateday", axis=1, inplace=True)


# Dataset
all_df = pd.read_csv("https://raw.githubusercontent.com/fathanahdz/submission-proyekDA-dicoding/master/Dashboard/all_data.csv")

all_df.sort_values(by="dateday", inplace=True)
all_df.reset_index(inplace=True)
all_df['dateday'] = pd.to_datetime(all_df['dateday'])

min_date = all_df["dateday"].min()
max_date = all_df["dateday"].max()

with st.sidebar:
    st.markdown("""Submission: Proyek Analisis Data - Dicoding""")
    
    # Menambahkan logo
    st.image("https://github.com/fathanahdz/submission-proyekDA-dicoding/blob/master/Dashboard/bikelogo.jpeg?raw=true")  #Image by freepik

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label = 'Rentang Waktu', 
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


main_df = all_df[(all_df['dateday'] >= str(start_date)) & (all_df['dateday'] <= str(end_date))]

monthly_df = create_monthly(main_df)
hourly_rental_df = create_hourly(main_df)
season_df = create_season(main_df)
weather_df = create_weather(main_df)

# UI
st.header('Teman Bike Analytic Dashboard 🚲✨')

# Subheader Average Bike Rentals Performance Over Time📈
st.subheader('Average Bike Rentals Performance Over Time📈')

fig, ax = plt.subplots(figsize=(12, 6))
                       
sns.lineplot(x="month", y="count",hue="year",data=monthly_df) 
ax.set_xlabel("Month")
ax.set_ylabel("Average Bike Rentals")
ax.set_xticks(ticks=range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
ax.grid(True, alpha =0.5)
ax.set_title("Average of Bike Rentals by Month", loc="center", fontsize=15)

st.pyplot(fig)

# Average Bike Rentals based on Hour⌛
st.subheader('Average Bike Rentals based on Hour ⌛')

time_intervals_labels = [f"{hour}"for hour in range(0, 24)]

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="hour", y="count", hue="year",data=hourly_rental_df) 
ax.set_xlabel("Hours")
ax.set_ylabel("Average Bike Rentals")
ax.set_xticks(ticks=range(24), labels=time_intervals_labels, rotation=45, ha='right')
ax.grid(True, alpha=0.5)
ax.set_title("Average of Bike Rentals by Hour in 2011 and 2012", loc="center", fontsize=15)

st.pyplot(fig)

# Bike Rentals Percentage based on Season🍂
st.subheader('Bike Rentals Percentage based on Season 🍂')

fig_season, ax_season = plt.subplots()
explode = (0.1, 0, 0, 0)

ax_season.pie(
    season_df['count'],
    labels = season_df['season'],
    autopct='%1.1f%%',
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red'],
    explode=explode
)

st.pyplot(fig_season)

# Bike Rentals Percentage based on Weather
st.subheader('Bike Rentals Percentage based on Weather ☁️')

fig_weather, ax_weather = plt.subplots()
explode = (0.1, 0, 0)

#Mengecualikan heavy rain karena nilainya 0.
filtered_weather_df = weather_df[weather_df['weather'] != 'Heavy Rain']

ax_weather.pie(
    filtered_weather_df['count'],
    labels=filtered_weather_df['weather'],
    autopct='%1.1f%%',
    colors=['tab:blue', 'tab:orange', 'tab:green', 'tab:red'],
    explode=explode
)

ax_weather.legend(filtered_weather_df['weather'], loc='upper right')
st.pyplot(fig_weather)

# Copyright
st.caption('Copyright (C) Nurunnisa Fathanah 2024')