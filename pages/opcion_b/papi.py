import streamlit as st

colores = ["#e74c3c", "#2980b9", "#27ae60", "#8e44ad", "#f39c12", "#ffffff"]  # rojo, azul, verde, púrpura, naranja, gris

def mostrar():
    st.title("📗 Calculadora de P.A.P.I. - Universidad Nacional de Colombia")
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
    st.write("Ingrese los datos de las asignaturas cursadas.")

    asignaturas = []
    total_creditos = 0
    total_ponderado = 0.0

    num_asignaturas = st.number_input("¿Cuántas asignaturas desea ingresar?", min_value=1, step=1)
    st.divider()

    for i in range(num_asignaturas):
        color = colores[i % len(colores)]
        st.markdown(f'<h3 style="color:{color}">📚 Asignatura {i + 1}</h3>', unsafe_allow_html=True)

        nombre = st.text_input(f"Nombre de la asignatura {i + 1}", key=f"nombre_{i}")
        creditos = st.number_input(f"Número de créditos", min_value=1, step=1, key=f"creditos_{i}")
        calificacion = st.number_input(f"Calificación obtenida (entre 0.0 y 5.0)", min_value=0.0, max_value=5.0, step=0.1, key=f"nota_{i}")
        st.caption("Nota: Ingresa un número etre 0 y 5.")

        asignaturas.append((nombre, creditos, calificacion))
        total_creditos += creditos
        total_ponderado += creditos * calificacion

    if st.button("Calcular P.A.P.P.I."):
            
        pappi = total_ponderado / total_creditos
        st.divider()
        st.markdown("### 📝 Resumen de asignaturas:")
        
        for i, (nombre, creditos, calif) in enumerate(asignaturas, 1):
            f"Calificación: {calif}"
            st.write(f"{i}. {nombre} - Créditos: {creditos}")

        st.markdown("### 📊 Resultado final:")
        st.write(f"**Sumatoria ponderada (Créditos × Calificación):** {total_ponderado:.1f}")
        st.write(f"**Total de créditos:** {total_creditos}")
        st.success(f"**P.A.P.I.:** {pappi:.3f}")
