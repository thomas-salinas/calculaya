import streamlit as st
import pandas as pd

colores = ["#e74c3c", "#2980b9", "#27ae60", "#8e44ad", "#f39c12", "#ffffff"]

def mostrar():
    st.title("📗 Organizador de horario")
    st.write("Esta herramienta te ayuda a organizar saber cuánto tiempo tienes que dedicar a cada asignatura.")
    
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona cuántas asignaturas deseas añadir
        2. Ingresa el nombre de la asignatura y los créditos
        3. Ingresa los días y horas en que tienes clases sincrónicas
        4. Presiona "Ver horario sugerido"
        5. Revisa cuántas horas sincrónicas y asincrónicas deberías tener
        """)
    
    st.divider()

    st.write("Ingrese los datos de las asignaturas que está cursando:")
    asignaturas = []
    num_asignaturas = st.number_input("¿Cuántas asignaturas desea ingresar?", min_value=1, step=1)
    st.divider()

    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

    for i in range(num_asignaturas):
        color = colores[i % len(colores)]
        st.markdown(f'<h3 style="color:{color}">📚 Asignatura {i + 1}</h3>', unsafe_allow_html=True)

        nombre = st.text_input(f"Nombre de la asignatura {i + 1}", key=f"nombre_{i}")
        creditos = st.number_input(f"Número de créditos", min_value=1, step=1, key=f"creditos_{i}")
        trabajo_semanal = creditos * 3  # (48 x créditos)/16 semanas

        # Horario sincrónico
        st.markdown("**Horario sincrónico**")
        dias_clase = st.multiselect(f"Días de clase ({nombre}):", dias_semana, key=f"dias_{i}")
        sincronicas = 0
        horas_por_dia = {}

        for d in dias_clase:
            col1, col2 = st.columns(2)
            with col1:
                inicio = st.time_input(f"Inicio {d} ({nombre})", key=f"inicio_{i}_{d}")
            with col2:
                fin = st.time_input(f"Fin {d} ({nombre})", key=f"fin_{i}_{d}")
            duracion = (pd.Timestamp.combine(pd.Timestamp.today(), fin) -
                        pd.Timestamp.combine(pd.Timestamp.today(), inicio)).seconds / 3600
            sincronicas += duracion
            horas_por_dia[d] = round(duracion, 2)

        asincronicas = max(0, trabajo_semanal - sincronicas)

        # Repartir asincrónicas de forma equitativa en los días restantes
        dias_libres = [d for d in dias_semana if d not in dias_clase]
        asincronicas_por_dia = {}
        if dias_libres:
            reparto = round(asincronicas / len(dias_libres), 2)
            for d in dias_libres:
                asincronicas_por_dia[d] = reparto
        else:
            # Si hay clase todos los días, no hay lugar para asincrónicas
            asincronicas_por_dia = {d: 0 for d in dias_semana}

        # Combinar ambos diccionarios (sincrónicas y asincrónicas)
        horario_total = []
        for d in dias_semana:
            sincr = horas_por_dia.get(d, 0)
            asincr = asincronicas_por_dia.get(d, 0)
            total_dia = sincr + asincr
            horario_total.append({
                "Día": d,
                "Horas sincrónicas": sincr,
                "Horas asincrónicas": asincr,
                "Total por día": round(total_dia, 2)
            })

        asignaturas.append({
            "Asignatura": nombre,
            "Créditos": creditos,
            "Total horas": trabajo_semanal,
            "Horas sincrónicas": round(sincronicas, 2),
            "Horas asincrónicas": round(asincronicas, 2),
            "Distribución": horario_total
        })
        st.divider()

    if st.button("Ver horario sugerido"):
        st.subheader("📋 Resumen general")
        resumen = [{
            "Asignatura": a["Asignatura"],
            "Créditos": a["Créditos"],
            "Horas sincrónicas": a["Horas sincrónicas"],
            "Horas asincrónicas": a["Horas asincrónicas"],
            "Total horas": a["Total horas"]
        } for a in asignaturas]
        st.dataframe(pd.DataFrame(resumen), use_container_width=True)

        st.info(f"🕒 Tiempo total semanal estimado: {sum(a['Total horas'] for a in asignaturas)} horas")
        st.caption("Nota: Actividad académica semanal = (48 × créditos) ÷ 16 semanas")

        # Mostrar distribución diaria por asignatura
        for a in asignaturas:
            st.markdown(f"### 📆 Distribución por días – {a['Asignatura']}")
            df_dias = pd.DataFrame(a["Distribución"])
            st.dataframe(df_dias, use_container_width=True)
            st.info(f"🕒 Se recomienda estudiar {total_dia} horas diarias.")
