import streamlit as st
from . import transmilenio

def pagina_principal():
    st.sidebar.title("Menú Opción B")
    seleccion = st.sidebar.radio(
        "Selecciona una sección:",
        ["Inicio", "Transmilenio"]
    )

    if seleccion == "Inicio":
        st.title("Opción B - Inicio")
        st.write("Contenido inicial para opción B.")
    elif seleccion == "Transmilenio":
        transmilenio.mostrar()


    if st.sidebar.button("⬅️ Volver al menú principal"):
        st.session_state.page = "menu"
