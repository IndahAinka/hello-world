import streamlit as st

st.title("Belajar Analisis Data")

# Membuat sidebar
with st.sidebar:

    st.text('Ini merupakan sidebar')

    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0,100)
    )
    st.write('Values:', values)

# Membuat Column
st.write("Contoh Penggunaan Column")
col1, col2, col3 = st.columns(3)
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")    

# Mengatur ukuran tampilan kolumn dengan perbandingan 2:1:1
st.write("Membuat kolum dengan perbandingan ukuran 2:1:1")
col1, col2, col3 = st.columns([2, 1, 1])
 
with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


#Membuat Tab
st.write('Belajar membuat Tab')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")