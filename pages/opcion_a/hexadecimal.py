import streamlit as st

def texto_a_hex(texto):
    return ' '.join(hex(ord(c))[2:] for c in texto)

def hex_a_texto(hexa):
    try:
        return ''.join(chr(int(h, 16)) for h in hexa.split())
    except ValueError:
        return "[Error: formato hexadecimal inválido]"

def mostrar():
    st.title("Conversor Texto ↔ Hexadecimal")
    modo = st.radio("Selecciona el modo:", ("Texto → Hexadecimal", "Hexadecimal → Texto"))

    if modo == "Texto → Hexadecimal":
        texto = st.text_input("Ingresa el texto:")
        if texto:
            resultado = texto_a_hex(texto)
            st.code(resultado, language="plaintext")
    else:
        hexa = st.text_input("Ingresa el código hexadecimal (separado por espacios):")
        if hexa:
            resultado = hex_a_texto(hexa)
            st.code(resultado, language="plaintext")
