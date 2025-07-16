import streamlit as st

def binario_a_decimal(bin_str):
    return int(bin_str, 2)

def decimal_a_binario(dec):
    return bin(dec)[2:]

def hexa_a_decimal(hex_str):
    return int(hex_str, 16)

def decimal_a_hexa(dec):
    return hex(dec)[2:].upper()

# Operaciones binarias
def operar_binarios(b1, b2, operacion):
    d1 = binario_a_decimal(b1)
    d2 = binario_a_decimal(b2)

    if operacion == 'Suma':
        resultado = d1 + d2
    elif operacion == 'Resta':
        resultado = d1 - d2
    elif operacion == 'Multiplicación':
        resultado = d1 * d2
    else:
        return "Operación inválida"

    return decimal_a_binario(resultado), resultado

# Operaciones hexadecimales
def operar_hexadecimales(h1, h2, operacion):
    d1 = hexa_a_decimal(h1)
    d2 = hexa_a_decimal(h2)

    if operacion == 'Suma':
        resultado = d1 + d2
    elif operacion == 'Resta':
        resultado = d1 - d2
    elif operacion == 'Multiplicación':
        resultado = d1 * d2
    else:
        return "Operación inválida"

    return decimal_a_hexa(resultado), resultado

def mostrar():
    st.title("🧮 Calculadora Binaria y Hexadecimal")

    st.write("""
    Esta calculadora permite realizar operaciones básicas (suma, resta, multiplicación) entre números en base binaria o hexadecimal.
    Además, muestra sus equivalentes en base decimal para facilitar la interpretación.
    """)

    with st.expander("Instrucciones de Uso", expanded=True):
        st.markdown("""
**1.** Selecciona si deseas trabajar en binario o hexadecimal.  
**2.** Ingresa los dos números en el sistema seleccionado.  
**3.** El sistema te mostrará los valores en base 10 y el resultado de la operación.  
**4.** Presiona **Calcular** para obtener el resultado.
""")
    st.divider()

    modo = st.selectbox("Selecciona el sistema", ["Binario", "Hexadecimal"])
    operacion = st.selectbox("Operación", ["Suma", "Resta", "Multiplicación"])

    if modo == "Binario":
        b1 = st.text_input("Primer número binario (ej: 1010)", "")
        if b1:
            try:
                dec_b1 = binario_a_decimal(b1)
                st.caption(f"Nota: este número es {dec_b1} en base 10.")
            except:
                st.caption("Entrada inválida")

        b2 = st.text_input("Segundo número binario (ej: 1101)", "")
        if b2:
            try:
                dec_b2 = binario_a_decimal(b2)
                st.caption(f"Nota: este número es {dec_b2} en base 10.")
            except:
                st.caption("Entrada inválida")

        if st.button("Calcular"):
            try:
                resultado_bin, resultado_dec = operar_binarios(b1, b2, operacion)
                st.success(f"Resultado en binario: {resultado_bin}")
                st.info(f"Resultado en decimal: {resultado_dec}")
            except:
                st.error("Entrada inválida. Asegúrate de ingresar binarios correctos.")

    else:
        h1 = st.text_input("Primer número hexadecimal (ej: A1)", "")
        if h1:
            try:
                dec_h1 = hexa_a_decimal(h1)
                st.caption(f"Nota: este número es {dec_h1} en base 10.")
            except:
                st.caption("Entrada inválida")

        h2 = st.text_input("Segundo número hexadecimal (ej: 2F)", "")
        if h2:
            try:
                dec_h2 = hexa_a_decimal(h2)
                st.caption(f"Nota: este número es {dec_h2} en base 10.")
            except:
                st.caption("Entrada inválida")

        if st.button("Calcular"):
            try:
                resultado_hex, resultado_dec = operar_hexadecimales(h1, h2, operacion)
                st.success(f"Resultado en hexadecimal: {resultado_hex}")
                st.info(f"Resultado en decimal: {resultado_dec}")
            except:
                st.error("Entrada inválida. Asegúrate de ingresar hexadecimales válidos.")
