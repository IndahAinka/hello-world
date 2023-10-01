import streamlit as st

# Membuat  Input Text
name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama : ', name)

# Membuat text area
text = st.text_area('Feedback')
st.write('Feedback :', text )