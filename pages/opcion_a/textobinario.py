import streamlit as st
def mostrar():
    def texto_a_binario(texto):
        return ' '.join(format(ord(c), '08b') for c in texto)

    def binario_a_texto(binario):
        try:
            caracteres = binario.split()
            return ''.join(chr(int(b, 2)) for b in caracteres)
        except ValueError:
            return "⚠️ Binario inválido."

    st.title("Conversor de Texto ⇄ Binario")

    opcion = st.radio("¿Qué quieres hacer?", ("Texto a Binario", "Binario a Texto"))

    if opcion == "Texto a Binario":
        texto = st.text_input("Ingresa el texto:")
        if texto:
            binario = texto_a_binario(texto)
            st.text_area("Resultado en binario:", binario, height=100)

    elif opcion == "Binario a Texto":
        binario = st.text_input("Ingresa el texto en binario (separado por espacios):")
        if binario:
            texto = binario_a_texto(binario)
            st.text_area("Texto recuperado:", texto, height=100)
