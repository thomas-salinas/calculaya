import streamlit as st

# Inicializar lista
if "datos" not in st.session_state:
    st.session_state.datos = []

def calcular_varianza(datos):
    n = len(datos)
    media = sum(datos) / n
    return sum((x - media) ** 2 for x in datos) / n

def calcular_desviacion_estandar(datos):
    varianza = calcular_varianza(datos)
    return varianza ** 0.5

def mostrar():
    st.title("📊 Calculadora de Varianza y Desviación Estándar")
    st.write("Este programa permite ingresar números uno a uno y calcular la varianza y desviación estándar.")

    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Ingresa un número y presiona Enter.
        2. Repite el paso anterior para todos los valores.
        3. Haz clic en "Calcular" cuando termines.
        4. Usa "Reiniciar" para empezar de nuevo.
        """)

    st.divider()

    # Formulario para añadir números (Enter funciona aquí)
    with st.form(key="formulario_numero", clear_on_submit=True):
        nuevo = st.number_input("Ingrese un número", step=1.0, format="%.4f", key="nuevo_input")
        submit = st.form_submit_button("Añadir")
        if submit:
            st.session_state.datos.append(nuevo)
    st.session_state.datos = []
    # Reiniciar
    if st.button("🔁 Reiniciar"):
        st.session_state.datos = []

    # Mostrar datos
    if st.session_state.datos:
        st.write("Números ingresados:")
        st.code(", ".join(str(x) for x in st.session_state.datos))

        if st.button("✅ Calcular"):
            datos = st.session_state.datos
            if len(datos) < 2:
                st.warning("Se necesitan al menos dos números.")
            else:
                var = calcular_varianza(datos)
                desv = calcular_desviacion_estandar(datos)
                st.success(f"Varianza: {var:.4f}")
                st.success(f"Desviación estándar: {desv:.4f}")
    else:
        st.info("Aún no hay datos.")
