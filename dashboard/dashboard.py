import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='white')

st.header('Dashboard Peminjaman Sepeda :sparkles:')
st.subheader('Pengaruh Cuaca Terhadap Peminjaman Sepeda')

day_df = pd.read_csv("D:/KULIAH/MSIB/Projek Akhir/data/day.csv")
hour_df = pd.read_csv("D:/KULIAH/MSIB/Projek Akhir/data/hour.csv")

data_tren_cuaca = day_df.groupby('weathersit').agg({
    'cnt': 'sum'
})

data_tren_bulan = day_df.groupby('mnth').agg({
    'cnt': 'sum'
})

fig1, ax1 = plt.subplots()
ax1.bar(data_tren_cuaca.index, data_tren_cuaca['cnt'], color=['lightblue', 'lightgreen', 'lightcoral', 'lightgray'])
ax1.set_xlabel('Situasi Cuaca')
ax1.set_ylabel('Jumlah Peminjaman')
ax1.set_title('Jumlah Peminjaman Sepeda Berdasarkan Situasi Cuaca')
st.pyplot(fig1)

st.subheader('Peminjaman Sepeda Berdasarkan Bulan')
fig2, ax2 = plt.subplots()
ax2.bar(data_tren_bulan.index, data_tren_bulan['cnt'], color='skyblue')
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Jumlah Peminjaman')
ax2.set_title('Jumlah Peminjaman Sepeda per Bulan')
st.pyplot(fig2)