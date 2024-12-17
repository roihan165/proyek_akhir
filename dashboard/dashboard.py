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
1. **Bagaimana tren jumlah pengguna sepeda (baik kasual maupun terdaftar) di setiap musim?**
2. **Bagaimana pengaruh faktor cuaca (suhu, kelembapan, dan kecepatan angin) terhadap jumlah total pengguna sepeda?**
""")

# Pertanyaan 1: Seasonal Trends for Casual and Registered Users
st.subheader("Pertanyaan 1: tren jumlah pengguna sepeda (baik kasual maupun terdaftar) di setiap musim")

# Visualization for Seasonal Trends
fig, ax = plt.subplots(figsize=(12, 6))
# Group data by season and calculate mean values for casual and registered users
seasonal_means = day_df_clean.groupby('season')[['casual', 'registered']].mean().reset_index()

# Plot side-by-side bar plot for casual and registered users
sns.barplot(x='season', y='casual', data=seasonal_means, label='Casual Users', color='blue', alpha=0.7)
sns.barplot(x='season', y='registered', data=seasonal_means, label='Registered Users', color='red', alpha=0.7)

ax.set_title("Tren Pengguna Sepeda (Kasual dan Terdaftar) di Setiap Musim", fontsize=14)
ax.set_xlabel("Musim (1: Winter, 2: Summer, 3: Fall, 4: Spring)", fontsize=12)
ax.set_ylabel("Rata-rata Jumlah Pengguna Sepeda", fontsize=12)
ax.legend()
st.pyplot(fig)


st.markdown("""
**Insight**:
- Tren Musiman Pengguna Kasual dan Terdaftar:
Dari grafik, kita bisa melihat bahwa baik pengguna kasual maupun pengguna terdaftar lebih banyak menggunakan sepeda selama musim panas (summer) dan gugur (fall). Penggunaan sepeda paling rendah terjadi pada musim dingin (winter).
- Pengguna terdaftar lebih stabil sepanjang musim, tetapi ada penurunan pada musim dingin.
- Pengguna kasual menunjukkan fluktuasi yang lebih besar, dengan lonjakan penggunaan pada musim panas dan penurunan tajam di musim dingin.
- Interpretasi: Ini menunjukkan bahwa pengguna terdaftar cenderung lebih sering menggunakan sepeda terlepas dari musim, mungkin untuk bekerja atau keperluan sehari-hari, sementara pengguna kasual lebih dipengaruhi oleh cuaca atau kegiatan rekreasi.
""")

# Pertanyaan 2: Effect of Weather Factors on Total Bike Rentals
st.subheader("Pertanyaan 2: pengaruh faktor cuaca terhadap jumlah total pengguna sepeda")

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
- Plot ini menunjukkan korelasi positif: seiring meningkatnya suhu, jumlah pengguna sepeda juga meningkat hingga mencapai titik tertentu (sekitar 0.6–0.7 dalam skala ternormalisasi). Setelah titik ini, tren tampak mendatar atau sedikit menurun.
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
- Data menunjukkan tren sedikit menurun: kelembapan yang lebih tinggi tampaknya mengurangi jumlah pengguna sepeda. Sebagian besar jumlah pengguna yang tinggi terkonsentrasi pada tingkat kelembapan sedang (0.4 - 0.7).
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
- Titik data tampak tersebar tanpa pola yang jelas, menunjukkan bahwa tidak ada korelasi yang signifikan antara kecepatan angin dan jumlah pengguna sepeda.
""")

# Final summary
st.subheader("Kesimpulan")
st.markdown("""
1. **Pertanyaan 1**: Musim dan cuaca adalah dua faktor penting yang mempengaruhi pola penggunaan sepeda. Di musim panas dan gugur, Jadi langkah yang bisa dilakukan adalah operator perlu mempersiapkan lebih banyak sepeda, sementara di musim dingin bisa dilakukan strategi untuk menjaga atau meningkatkan minat pengguna atau dengan mengurangi jumlah sepada yang direntalkan.
2. **Pertanyaan 2**: Cuaca, terutama suhu, memiliki pengaruh besar terhadap jumlah rental sepeda. Dengan menggunakan prediksi cuaca dan menyesuaikan distribusi sepeda serta strategi promosi, operator dapat memaksimalkan keuntungan dan efisiensi layanan sepanjang tahun. jadi langkah yang bisa dilakukan adalah Fokus pada promosi aktivitas bersepeda selama rentang suhu sedang (kondisi yang optimal untuk kenyamanan pengguna).Kurangi dampak negatif kelembapan dengan menyediakan tips atau infrastruktur pendukung (misalnya, area teduh, stasiun air minum).
""")
