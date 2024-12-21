import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset (ensure these files are available)
hour_df_clean = pd.read_csv('..\data\hour_clean.csv')

# Memuat data
@st.cache_data  # Perbarui dekorator caching
def load_data():
    data = pd.read_csv('..\data\day_clean.csv')  # Ganti dengan path yang sesuai jika perlu
    return data

# Memanggil fungsi untuk memuat data
data = load_data()

# Set up the Streamlit dashboard
st.title("Bike Sharing Data Dashboard")

# Introduction
st.markdown("""
This dashboard explores two key questions:
1. **Bagaimana tren jumlah pengguna sepeda di setiap musim per tahun?**
2. **Bagaimana pengaruh faktor cuaca (suhu, kelembapan, dan kecepatan angin) terhadap jumlah total pengguna sepeda?**
""")

year_mapping = {0: '2011', 1: '2012'}


# User input for selecting years to display
years = st.multiselect(
    "Pilih Tahun:",
    options=[0, 1],  # Assuming 0 is for 2011 and 1 is for 2012 (as per your data)
    format_func=lambda x:year_mapping[x],
    default=[0,1]
)

# Create a pivot table for the data
pivot_df = data.pivot_table(index='season', columns='yr', values='cnt', aggfunc='sum')
# Filter the pivot table based on selected years
pivot_df_filtered = pivot_df[years]

# Create a side-by-side bar plot for the selected years

# Streamlit Title
st.title("Tren Pengguna Sepeda Berdasarkan Musim dan Tahun")

# Display a description or any introductory text
st.write("""
Visualisasi di bawah ini menunjukkan tren penggunaan sepeda berdasarkan musim dan tahun.
Dua tahun yang dibandingkan adalah 2011 (yr=0) dan 2012 (yr=1), dengan data musim yang mencakup Winter, Summer, Fall, dan Spring.
""")

# Create a side-by-side bar plot for the selected years
fig, ax = plt.subplots(figsize=(12, 6))
pivot_df_filtered.plot(kind='bar', ax=ax, alpha=0.7, width=0.8)

# Customize the plot
ax.set_title("Tren Pengguna Sepeda Berdasarkan Musim dan Tahun", fontsize=14)
ax.set_xlabel("Musim (1: Winter, 2: Summer, 3: Fall, 4: Spring)", fontsize=12)
ax.set_ylabel("Total Pengguna Sepeda", fontsize=12)
ax.set_xticks(range(len(pivot_df_filtered.index)))  # Ensure the x-axis labels are horizontal
ax.set_xticklabels(pivot_df_filtered.index, rotation=0)
ax.legend([f"{2011 if year == 0 else 2012} (yr={year})" for year in years], title="Tahun", fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot in Streamlit
st.pyplot(fig)


st.markdown("""
**Insight**:
- Tren Musiman Tahun 2011 dan 2012: Dari grafik, kita bisa melihat bahwa baik tahun 2011 maupun tahun 2012 pengguna lebih banyak menggunakan sepeda selama musim panas (summer) dan gugur (fall). Penggunaan sepeda paling rendah terjadi pada musim dingin (winter)
- Serta Kita dapat melihat peningkatan jumlah rental pada tahun 2012 dari tahun sebelumnya
""")

# Pertanyaan 2: Effect of Weather Factors on Total Bike Rentals
weather_factors = ['temp', 'hum', 'windspeed', 'cnt']
correlation_matrix = hour_df_clean[weather_factors].corr()

# Streamlit Title
st.title("Korelasi Faktor Cuaca terhadap Pengguna Sepeda")

# Display the correlation matrix heatmap
st.write("### Matriks Korelasi: Faktor Cuaca dan Total Pengguna Sepeda")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Add titles and labels
plt.title("Correlation Matrix: Weather Factors and Total Users", fontsize=14)
plt.xlabel("Variables", fontsize=12)
plt.ylabel("Variables", fontsize=12)

# Display the heatmap in Streamlit
st.pyplot(plt)

# Bar Graph for correlations with 'cnt'
correlations = correlation_matrix['cnt'].drop('cnt')

# Plot the bar graph
st.write("### Korelasi Faktor Cuaca terhadap Total Pengguna Sepeda")
plt.figure(figsize=(8, 6))
correlations.plot(kind='bar', color=['red', 'blue', 'green'], alpha=0.8)

# Add titles and labels
plt.title("Korelasi Faktor Cuaca terhadap Total Pengguna Sepeda", fontsize=14)
plt.xlabel("Faktor Cuaca", fontsize=12)
plt.ylabel("Koefisien Korelasi", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the bar graph in Streamlit
st.pyplot(plt)

st.markdown("""
**Insight**:
- - Suhu (temp):

Memiliki korelasi yang kuat dengan total pengguna sepeda, menunjukkan pengaruh yang signifikan.
- Kelembapan (hum):

Korelasi negatif menunjukkan bahwa kelembapan yang lebih tinggi cenderung mengurangi penggunaan sepeda
- Kecepatan Angin (windspeed):

Korelasi positif yang lemah menunjukkan pengaruh yang lebih kecil terhadap penggunaan sepeda.
""")
# Final summary
st.subheader("Kesimpulan")
st.markdown("""
1. **Pertanyaan 1**: Musim adalah faktor penting yang mempengaruhi pola penggunaan sepeda setiap tahun. Di musim panas dan gugur, Jadi langkah yang bisa dilakukan adalah operator perlu mempersiapkan lebih banyak sepeda, sementara di musim dingin bisa dilakukan strategi untuk menjaga atau meningkatkan minat pengguna atau dengan mengurangi jumlah sepada yang direntalkan.
2. **Pertanyaan 2**: Cuaca, terutama suhu, memiliki pengaruh besar terhadap jumlah rental sepeda. Operator dapat memaksimalkan keuntungan dan efisiensi layanan, jadi langkah yang bisa dilakukan adalah Fokus pada promosi aktivitas bersepeda selama rentang suhu sedang (kondisi yang optimal untuk kenyamanan pengguna).Kurangi dampak negatif kelembapan dengan menyediakan tips atau infrastruktur pendukung (misalnya, area teduh, stasiun air minum).
""")
