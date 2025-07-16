import streamlit as st

def texto_a_hex(texto):
    return ' '.join(hex(ord(c))[2:] for c in texto)

def hex_a_texto(hexa):
    try:
        return ''.join(chr(int(h, 16)) for h in hexa.split())
    except ValueError:
        return "[Error: formato hexadecimal inválido]"

def mostrar():
    st.title("🖥️ Conversor Texto ↔ Hexadecimal")
    st.write("Herramienta para convertir texto a hexadecimal")

    st.write("\n")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona si quieres convertir texto a hexadecimal o hexadecimal a texto.
        2. Si escoges hexadecimal a texto, ingresa cada palabra en hexadecimal separada por espacios.
        3. Presiona enter para ver resultados
        """)
    st.divider()

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
