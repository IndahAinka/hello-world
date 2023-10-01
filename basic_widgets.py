import datetime
import streamlit as st
import pandas as pd

# Membuat  Input Text
name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama : ', name)

# Membuat text area
text = st.text_area('Feedback')
st.write('Feedback :', text )

# Membuat number input
number = st.number_input(label='Umur')
st.write('Umur :', int(number), ' tahun')

# Membuat date input
date = st.date_input(label='Tanggal Lahir', min_value=datetime.date(1900,1,1))
st.write('Tanggal Lahir :', date)

# Mengupload File
uploaded_file = st.file_uploader('Choose a csv file')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)