import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='white')

st.header('Dashboard Peminjaman Sepeda :sparkles:')
st.subheader('Pengaruh Cuaca Terhadap Peminjaman Sepeda')

day_hour_df = pd.read_csv("dashboard/data_all.csv")

day_hour_df['dteday'] = pd.to_datetime(day_hour_df['dteday'])
day_hour_df['year'] = day_hour_df['dteday'].dt.year
day_hour_df['month'] = day_hour_df['dteday'].dt.month
day_hour_df['day_type'] = np.where(day_hour_df['weekday'] == 1, 'workingday', 'weekend')

data_tren_hari = day_hour_df.groupby('day_type')['cnt'].sum().reset_index()
data_2012 = day_hour_df[day_hour_df['year'] == 2012]
data_tren_bulan_2012 = data_2012.groupby('month').agg({'cnt': 'sum'}).reset_index()

st.subheader('Perbandingan Peminjaman Sepeda antara Weekday dan Weekend')
fig1, ax1 = plt.subplots()
ax1.bar(data_tren_hari['day_type'], data_tren_hari['cnt'], color=['blue', 'orange'], alpha=0.7)
ax1.set_title('Perbandingan Peminjaman Sepeda antara Weekday dan Weekend')
ax1.set_xlabel('Jenis Hari')
ax1.set_ylabel('Jumlah Peminjaman')
ax1.grid(axis='y')
st.pyplot(fig1)

st.subheader('Jumlah Peminjaman Sepeda per Bulan di Tahun 2012')
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(data_tren_bulan_2012['month'], data_tren_bulan_2012['cnt'], color='b', alpha=0.6)
ax2.set_xticks(data_tren_bulan_2012['month'])
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.set_title('Jumlah Peminjaman Sepeda per Bulan di Tahun 2012')
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Jumlah Peminjaman')
ax2.grid(True)
plt.tight_layout()
st.pyplot(fig2)