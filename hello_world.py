import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Belajar Analisis Data')

st.header("Pengembangan Dashboard")

st.subheader('Pengembangan Dashboard')
 
st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# Membuat Table
st.write(
    "Table dibawah ini  dibuat menggunakan  table :"
)
st.table(data=df)

st.write(
    "Table dibawah ini dibuat menggunakan dataframe : "
)
# Membuat dataFrame
st.dataframe(data=df, width=500, height=150)


# Menampilkan code
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

# Menampilkan Teks
st.text('Halo, calon praktisi data masa depan.')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

st.write(
    "Tabel dibawah ini dibuat menggunakan matriks"
)
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")


st.write(
    "Function json() untuk menampilkan data dalam format JSON."
)
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})


st.write(
    "Berikut contoh chart menggunakan streamlit"
)
#Perintah di bawah ini digunakan untuk membuat Chart
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

# Untuk menampilkan caption pada bagian bawah page
st.caption('Copyright (c) 2023')





