import streamlit as st

def descifrar_cesar(texto, K):
    resultado = []
    for caracter in texto:
        if caracter.isalpha() and caracter.isupper():
            nuevo_caracter = chr(((ord(caracter) - ord('A') - K) % 26 + ord('A')))
            resultado.append(nuevo_caracter)
        else:
            resultado.append(caracter)
    return ''.join(resultado)

def mostrar():
    st.title("⚫ Descifrado César (solo mayúsculas A-Z) ⚫")

    st.write("Herramienta para decifrar el cifrado César.")
    st.write("\n")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona el desplazamiento K.
        2. Ingresa renglón por renglón el mensaje.
        3. Presiona el botón "Descifrar" para ver el resultado.
        """)
    st.divider()
    k = st.number_input("Valor de K (desplazamiento)", min_value=0, max_value=25, value=3)

    texto_entrada = st.text_area("Introduce las líneas cifradas (una por línea)", height=200)

    if st.button("Descifrar"):
        lineas = texto_entrada.strip().split("\n")
        lineas_descifradas = [descifrar_cesar(linea.strip(), k) for linea in lineas]
        mensaje_final = ' '.join(lineas_descifradas)
        st.subheader("Resultado:")
        st.code(mensaje_final, language="plaintext")