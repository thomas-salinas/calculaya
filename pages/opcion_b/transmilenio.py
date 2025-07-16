import streamlit as st

def calcular_pasaje(dias):
    return 3200 * dias

def cuanto_alcanza(plata):
    pasajes = plata // 3200
    sobra = plata % 3200
    return pasajes, sobra

def mostrar():
    st.title("🚌 Calculadora de Pasajes")
    st. write("Esta herramienta calcula el costo de pasajes o cuántos puedes comprar con el dinero que tienes.")
    st.write("\n")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona cuántas asignaturas deseeas añadir
        2. Ingresa el nombre de la asignatura, creditos y la calificación obtenida
        3. Presiona el botón "Calcular P.A.P.I", el programa lo hará automaticamente
        4. Lee tus resultados en la parte inferior
        """)
    st.divider()


    tipo = st.radio("¿Qué información tienes?", ("📅 Número de días", "💸 Cantidad de dinero"))

    if tipo == "📅 Número de días":
        dias = st.number_input("Ingrese el número de días:", min_value=1, step=1)
        ida_y_vuelta = st.checkbox("¿Viaja ida y vuelta?")

        if st.button("Calcular total"):
            total = calcular_pasaje(dias) * 2 if ida_y_vuelta else calcular_pasaje(dias)
            st.success(f"💰 Total a pagar: ${total}")
    
    else:  # tipo == "Cantidad de dinero"
        dinero = st.number_input("Ingrese con cuánto dinero cuenta:", min_value=0, step=100)

        if st.button("Calcular cuántos pasajes alcanza"):
            pasajes, sobrante = cuanto_alcanza(dinero)
            st.info(f"Número de pasajes: {pasajes}")
            st.info(f"Dinero sobrante: ${sobrante}")
