import streamlit as st

st.set_page_config(page_title="App.py")
st.title("Hello, World!")
st.write("Selamat datang di aplikasi Streamlit")

name = st.text_input("Masukkan nama Anda:")
if name:
    st.write(f"Halo, {name}!")
