import streamlit as st
import pandas as pd

st.title("🗨️🗨️Website Developing using Python🗨️🗨️")
st.header("💟💟Website Developing using Python💟💟")

st.image('./img/jaynat.jpg')
st.subheader("Nattiwut Nongnuch")

dt=pd.read_csv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))