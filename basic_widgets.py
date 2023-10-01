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

# Membuat camera input
picture = st.camera_input('Take a picture')

if picture:
    st.image(picture)

st.title('Button Widgets')

# Membuat Button
if st.button('Say Hello'):
    st.write('Hello There')

# Membuat CheckBox
agree = st.checkbox('I Agree')

if agree:
    st.write('Welcome to my App')

# Menambahkan radio buton
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy','Drama','Documentary'),
    horizontal= False
)

if genre:
    st.write(genre)