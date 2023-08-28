import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por Luis F. Lopez")

# Pregunta al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Verifica si el usuario ha ingresado un nombre
if nombre_usuario:
    # Muestra el mensaje de bienvenida
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.
