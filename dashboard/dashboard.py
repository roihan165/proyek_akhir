import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset (ensure these files are available)
day_df_clean = pd.read_csv('..\data\day_clean.csv')

# Set up the Streamlit dashboard
st.title("Bike Sharing Data Dashboard")

# Introduction
st.header("Exploratory Data Analysis of Bike Sharing Data")
st.markdown("""
This dashboard explores two key questions:
1. **How do bike rentals (casual and registered users) vary across seasons?**
2. **How do weather factors (temperature, humidity, and windspeed) affect total bike rentals?**
""")

# Pertanyaan 1: Seasonal Trends for Casual and Registered Users
st.subheader("Pertanyaan 1: Seasonal Trends in Bike Rentals (Casual and Registered Users)")

# Visualization for Seasonal Trends
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='season', y='casual', data=day_df_clean, ci=None, label='Casual Users', color='orange', ax=ax)
sns.barplot(x='season', y='registered', data=day_df_clean, ci=None, label='Registered Users', color='blue', ax=ax)
ax.set_title("Tren Pengguna Sepeda (Kasual dan Terdaftar) di Setiap Musim")
ax.set_xlabel("Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)")
ax.set_ylabel("Jumlah Pengguna Sepeda")
ax.legend()
st.pyplot(fig)

st.markdown("""
**Insight**:
- Both casual and registered users rent more bikes during **Summer (2)** and **Fall (3)**, with rentals being significantly lower in Winter.
- Registered users have more consistent usage across seasons compared to casual users, who show greater seasonal variability.
""")

# Pertanyaan 2: Effect of Weather Factors on Total Bike Rentals
st.subheader("Pertanyaan 2: Effect of Weather Factors on Total Bike Rentals")

# Visualization for Temperature vs Total Users
st.markdown("### Pengaruh Suhu terhadap Jumlah Total Pengguna Sepeda")
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df_clean, color='red', ax=ax)
ax.set_title("Pengaruh Suhu terhadap Jumlah Total Pengguna Sepeda")
ax.set_xlabel("Suhu (Skala Ternormalisasi)")
ax.set_ylabel("Jumlah Total Pengguna Sepeda")
st.pyplot(fig)

st.markdown("""
**Insight**:
- There is a strong positive correlation between temperature and total bike rentals. Warmer temperatures lead to higher bike rentals.
""")

# Visualization for Humidity vs Total Users
st.markdown("### Pengaruh Kelembapan terhadap Jumlah Total Pengguna Sepeda")
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='hum', y='cnt', data=day_df_clean, color='blue', ax=ax)
ax.set_title("Pengaruh Kelembapan terhadap Jumlah Total Pengguna Sepeda")
ax.set_xlabel("Kelembapan (Skala Ternormalisasi)")
ax.set_ylabel("Jumlah Total Pengguna Sepeda")
st.pyplot(fig)

st.markdown("""
**Insight**:
- Higher humidity levels are associated with a slight decrease in total bike rentals. This might be because biking becomes uncomfortable on humid days.
""")

# Visualization for Windspeed vs Total Users
st.markdown("### Pengaruh Kecepatan Angin terhadap Jumlah Total Pengguna Sepeda")
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='windspeed', y='cnt', data=day_df_clean, color='green', ax=ax)
ax.set_title("Pengaruh Kecepatan Angin terhadap Jumlah Total Pengguna Sepeda")
ax.set_xlabel("Kecepatan Angin (Skala Ternormalisasi)")
ax.set_ylabel("Jumlah Total Pengguna Sepeda")
st.pyplot(fig)

st.markdown("""
**Insight**:
- As windspeed increases, the number of bike rentals decreases slightly, which could be due to the challenge of biking in windy conditions.
""")

# Final summary
st.subheader("Kesimpulan")
st.markdown("""
1. **Seasonal Effects**: Bike rentals peak in **Summer** and **Fall**, with **Winter** seeing a sharp decline, especially among casual users.
2. **Weather Factors**: 
   - **Temperature** has the most significant effect, with higher temperatures leading to more rentals.
   - **Humidity** and **windspeed** have negative but less significant impacts.
""")
