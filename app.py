import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("YARDAS_PASOS_DATOS_TICS.xlsx", index_col=0)

st.title("Este es un análisis estadístico")
st.header("Base de datos Yardas vs. Pases")
st.dataframe(df.head())
#Estadística descriptiva
st.header("Estadística descriptiva")
st.dataframe(df.describe())
df.columns = [ c.title().replace(" ","_") for  c in df.columns]

#Diagrama de caja y bigote de las yardas totales
fig, ax = plt.subplots()
ax.boxplot(df["Yardas_Totales"])
st.header("Diagrama de caja y bigote de yardas totales")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.boxplot(df["Pases_Completos"])
st.header("Diagrama de caja y bigote de pases completos")
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1 : 
  fig, ax = plt.subplots()
  ax.boxplot(df["Yardas_Totales"])
  st.header("Diagrama de caja y bigote de yardas totales")
  st.pyplot(fig)
with col2: 
  fig, ax = plt.subplots()
  ax.boxplot(df["Pases_Completos"])
  st.header("Diagrama de caja y bigote de pases completos")
  st.pyplot(fig)