import streamlit as st
from functions import calcular_media

st.title("Calcular Média")
st.subheader("Entrada das notas 1 e 2")

nota1 = st.text_input("Nota 1")
nota2 = st.text_input("Nota 2")


if st.button('Calcular'):
    media = calcular_media(nota1, nota2)
    st.write(f"Média: {float(media):.2f}")