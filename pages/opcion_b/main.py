import streamlit as st
from . import papi, transmilenio, comedores, dobletitulacion, monitorias, lugares_estudio, horario_estudio

def pagina_principal():
    st.sidebar.title("Menú Calculadoras Personales")
    seleccion = st.sidebar.radio(
        "Selecciona una calculadora:",
        ["Inicio","Calculadora P.A.P.I", "Calculadora transmilenio", "Comedores", "Doble titulación", "Horario monitorias",
        "Lugar para estudiar", "Organizador de horario"]
    )

    if seleccion == "Inicio":
        st.title("🏠 Calculadoras personales - Inicio")
        st.subheader("Bienvenido. Para utilizar las calculadoras, dirígete al menú de la izquierda y selecciona la opción que necesites.")

    elif seleccion == "Calculadora P.A.P.I":
        papi.mostrar()

    elif seleccion == "Calculadora transmilenio":
        transmilenio.mostrar()

    elif seleccion == "Comedores":
        comedores.mostrar()

    elif seleccion == "Doble titulación":
        dobletitulacion.mostrar()

    elif seleccion == "Horario monitorias":
        monitorias.mostrar()

    elif seleccion == "Lugar para estudiar":
        lugares_estudio.mostrar()

    elif seleccion == "Organizador de horario":
        horario_estudio.mostrar()

    if st.sidebar.button("⬅️ Volver al menú principal"):
        st.session_state.page = "menu"