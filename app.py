import streamlit as st
import pandas as pd

st.header("Ma première application !")
st.write("Mineure numérique - Laura")

nombres = [1, 2, 4, 7]
carre = [1**2, 2**2, 4**2, 7**2]

d = {"nombres" : nombres, "carré" : carre}
data = pd.DataFrame(d)

st.dataframe(data)
