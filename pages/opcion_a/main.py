import streamlit as st

from . import textobinario,morse, hexadecimal, cesar, ecuaciones_2x2_3x3, euleredos, trapeciosimpson, interpolacion_lagrange, runge_kutta, Newton_Raphson
from . import hexa_binario, desviacion_estandar

def pagina_principal():
    st.sidebar.title("🎓 Menú calculadoras académicas")
    seleccion = st.sidebar.radio(
        "Selecciona una calculadora:",
        ["Inicio", "Texto a binario", "Texto a Hexadecimal","Traductor Morse","Cifrado César","Calculadora hexa-binario","Calculadora ecuaciones 2x2 y 3x3",
        "Metodo Euler para EDOS","Trapecio o Simpson para integrales","Interpolación de Lagrange", "Calculadora Runge Kutta",
        "Newton-Raphson","Calculadora de Varianza y Desviación Estándar"]
    )


    #OPCIONES

    if seleccion == "Inicio":
        st.title("🎓 Calculadoras académicas - Inicio")
        st.write("Bienvenido. Para utilizar las calculadoras, dirígete al menú de la izquierda y selecciona la opción que necesites.")

    elif seleccion == "Texto a binario":
        textobinario.mostrar()
    
    elif seleccion == "Texto a Hexadecimal":
        hexadecimal.mostrar()

    elif seleccion == "Traductor Morse":
        morse.mostrar()
    
    elif seleccion == "Cifrado César":
        cesar.mostrar()

    elif seleccion == "Calculadora hexa-binario":
        hexa_binario.mostrar()

    elif seleccion == "Calculadora ecuaciones 2x2 y 3x3":
        ecuaciones_2x2_3x3.mostrar()
    
    elif seleccion == "Metodo Euler para EDOS":
        euleredos.mostrar()
    
    elif seleccion == "Trapecio o Simpson para integrales":
        trapeciosimpson.mostrar()
    
    elif seleccion == "Interpolación de Lagrange":
        interpolacion_lagrange.mostrar()

    elif seleccion == "Calculadora Runge Kutta":
        runge_kutta.mostrar()
    
    elif seleccion == "Newton-Raphson":
        Newton_Raphson.mostrar()

    elif seleccion == "Newton-Raphson":
        Newton_Raphson.mostrar()
    
    elif seleccion == "Calculadora de Varianza y Desviación Estándar":
        desviacion_estandar.mostrar()

    if st.sidebar.button("⬅️ Volver al menú principal"):
        st.session_state.page = "menu"