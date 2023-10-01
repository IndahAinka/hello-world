import streamlit as st

name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama : ', name)