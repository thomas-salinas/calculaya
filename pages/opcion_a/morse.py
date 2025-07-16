import streamlit as st

MORSE = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',   'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',   'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..',  '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

MORSE_INV = {v: k for k, v in MORSE.items()}

def texto_a_morse(texto):
    texto = texto.lower()
    return ' '.join(MORSE[c] for c in texto if c in MORSE)

def morse_a_texto(morse):
    return ''.join(MORSE_INV.get(c, '') for c in morse.split())

def mostrar():
    st.title("⚫ Traductor de Código Morse ⚫")
    st.write("Herramienta para traducir morse.")
    st.write("\n")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona si quieres convertir texto a morse o morse a texto.
        2. Si escoges morse a texto, NO ingreses tildes.
        3. Presiona enter para ver resultados.
        """)
    st.divider()

    modo = st.radio("Selecciona el modo:", ("Texto → Morse", "Morse → Texto"))
    if modo == "Texto → Morse":
        texto = st.text_input("Escribe el texto a convertir (no uses tildes):")
        if texto:
            morse = texto_a_morse(texto)
            st.code(morse, language="plaintext")
    else:
        morse = st.text_input("Escribe el código Morse a traducir (usa espacios entre letras):")
        if morse:
            texto = morse_a_texto(morse)
            st.code(texto, language="plaintext")
