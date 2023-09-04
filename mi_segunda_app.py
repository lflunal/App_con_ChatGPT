import streamlit as st

# Título de la app
st.title("Mi Segunda App - Conversor Universal")

# Autor de la app
st.write("Esta app fue elaborada por Luis F. Lopez")

# Selección del tipo de conversión
conversor = st.selectbox("Selecciona el tipo de conversión:",
                         ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius",
                          "Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas",
                          "Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas",
                          "Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas",
                          "Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días",
                          "Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo",
                          "Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados",
                          "Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora",
                          "Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Barras",
                          "Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"])

# Función para realizar la conversión de temperatura
def convertir_temperatura(valor, tipo):
    if tipo == "Celsius a Fahrenheit":
        return (valor * 9/5) + 32
    elif tipo == "Fahrenheit a Celsius":
        return (valor - 32) * 5/9
    elif tipo == "Celsius a Kelvin":
        return valor + 273.15
    elif tipo == "Kelvin a Celsius":
        return valor - 273.15

# Función para realizar la conversión de longitud
def convertir_longitud(valor, tipo):
    if tipo == "Pies a Metros":
        return valor * 0.3048
    elif tipo == "Metros a Pies":
        return valor / 0.3048
    elif tipo == "Pulgadas a Centímetros":
        return valor * 2.54
    elif tipo == "Centímetros a Pulgadas":
        return valor / 2.54

# Función para realizar la conversión de peso/masa
def convertir_peso(valor, tipo):
    if tipo == "Libras a Kilogramos":
        return valor * 0.453592
    elif tipo == "Kilogramos a Libras":
        return valor / 0.453592
    elif tipo == "Onzas a Gramos":
        return valor * 28.3495
    elif tipo == "Gramos a Onzas":
        return valor / 28.3495

# Función para realizar la conversión de volumen
def convertir_volumen(valor, tipo):
    if tipo == "Galones a Litros":
        return valor * 3.78541
    elif tipo == "Litros a Galones":
        return valor / 3.78541
    elif tipo == "Pulgadas cúbicas a Centímetros cúbicos":
        return valor * 16.3871
    elif tipo == "Centímetros cúbicos a Pulgadas cúbicas":
        return valor / 16.3871

# Función para realizar la conversión de tiempo
def convertir_tiempo(valor, tipo):
    if tipo == "Horas a Minutos":
        return valor * 60
    elif tipo == "Minutos a Segundos":
        return valor * 60
    elif tipo == "Días a Horas":
        return valor * 24
    elif tipo == "Semanas a Días":
        return valor * 7

# Función para realizar la conversión de velocidad
def convertir_velocidad(valor, tipo):
    if tipo == "Millas por hora a Kilómetros por hora":
        return valor * 1.60934
    elif tipo == "Kilómetros por hora a Metros por segundo":
        return valor * 0.277778
    elif tipo == "Nudos a Millas por hora":
        return valor * 1.15078
    elif tipo == "Metros por segundo a Pies por segundo":
        return valor * 3.28084

# Función para realizar la conversión de área
def convertir_area(valor, tipo):
    if tipo == "Metros cuadrados a Pies cuadrados":
        return valor * 10.7639
    elif tipo == "Pies cuadrados a Metros cuadrados":
        return valor / 10.7639
    elif tipo == "Kilómetros cuadrados a Millas cuadradas":
        return valor * 0.386102
    elif tipo == "Millas cuadradas a Kilómetros cuadrados":
        return valor / 0.386102

# Función para realizar la conversión de energía
def convertir_energia(valor, tipo):
    if tipo == "Julios a Calorías":
        return valor * 0.239006
    elif tipo == "Calorías a Kilojulios":
        return valor * 0.004184
    elif tipo == "Kilovatios-hora a Megajulios":
        return valor * 3.6
    elif tipo == "Megajulios a Kilovatios-hora":
        return valor / 3.6

# Función para realizar la conversión de presión
def convertir_presion(valor, tipo):
    if tipo == "Pascales a Atmósferas":
        return valor * 0.00000987
    elif tipo == "Atmósferas a Pascales":
        return valor * 101325
    elif tipo == "Barras a Libras por pulgada cuadrada":
        return valor * 14.5038
    elif tipo == "Libras por pulgada cuadrada a Barras":
        return valor / 14.5038
def convertir_datos(valor, tipo):
    if tipo == "Megabytes a Gigabytes":
        return valor / 1024
    elif tipo == "Gigabytes a Terabytes":
        return valor / 1024
    elif tipo == "Kilobytes a Megabytes":
        return valor / 1024
    elif tipo == "Terabytes a Petabytes":
        return valor / 1024

# Entrada del usuario para el valor a convertir
valor = st.number_input("Ingresa el valor a convertir:", step=0.01)

# Botón para realizar la conversión
if st.button("Convertir"):
    if conversor and valor:
        if "Celsius" in conversor or "Fahrenheit" in conversor or "Kelvin" in conversor:
            resultado = convertir_temperatura(valor, conversor)
            st.write(f"Resultado: {valor} grados {conversor.split(' a ')[0]} equivale a {resultado:.2f} grados {conversor.split(' a ')[1]}")
        elif "Pies" in conversor or "Metros" in conversor or "Pulgadas" in conversor or "Centímetros" in conversor:
            resultado = convertir_longitud(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Libras" in conversor or "Kilogramos" in conversor or "Onzas" in conversor or "Gramos" in conversor:
            resultado = convertir_peso(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Galones" in conversor or "Litros" in conversor or "Pulgadas cúbicas" in conversor or "Centímetros cúbicos" in conversor:
            resultado = convertir_volumen(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Horas" in conversor or "Minutos" in conversor or "Días" in conversor or "Semanas" in conversor:
            resultado = convertir_tiempo(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Millas por hora" in conversor or "Kilómetros por hora" in conversor or "Nudos" in conversor or "Metros por segundo" in conversor:
            resultado = convertir_velocidad(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Metros cuadrados" in conversor or "Pies cuadrados" in conversor or "Kilómetros cuadrados" in conversor or "Millas cuadradas" in conversor:
            resultado = convertir_area(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Julios" in conversor or "Calorías" in conversor or "Kilovatios-hora" in conversor or "Megajulios" in conversor:
            resultado = convertir_energia(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Pascales" in conversor or "Atmósferas" in conversor or "Barras" in conversor or "Libras por pulgada cuadrada" in conversor:
            resultado = convertir_presion(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
        elif "Megabytes" in conversor or "Gigabytes" in conversor or "Kilobytes" in conversor or "Terabytes" in conversor:
            resultado = convertir_datos(valor, conversor)
            st.write(f"Resultado: {valor} {conversor.split(' a ')[0]} equivale a {resultado:.2f} {conversor.split(' a ')[1]}")
