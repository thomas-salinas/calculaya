import streamlit as st
import re

# ======================
# FUNCIONES DE PROCESAMIENTO
# ======================
def parse_curriculum(text):
    courses = {}
    for line in text.strip().split('\n'):
        tokens = line.split()
        if len(tokens) < 4:
            continue
            
        # Buscar el indice de los creditos (ultimo numero en la linea)
        credit_index = None
        for i in range(len(tokens)-1, 0, -1):
            if tokens[i].isdigit():
                credit_index = i
                break
                
        if credit_index is None:
            continue
            
        code = tokens[0]
        creditos = int(tokens[credit_index])
        nombre = " ".join(tokens[1:credit_index])
        componente = " ".join(tokens[credit_index+1:])
        
        courses[code] = {'nombre': nombre, 'creditos': creditos, 'componente': componente}
    return courses

def parse_student_history(text):
    history = {}
    for line in text.strip().split('\n'):
        if ',' in line:
            parts = [p.strip() for p in line.split(',')]
        else:
            parts = re.split(r'\s{2,}', line.strip())
        
        if len(parts) >= 4:
            code = parts[0]
            name = parts[1] if len(parts) > 4 else " ".join(parts[1:-2])
            try:
                credits = int(parts[-2])
            except ValueError:
                credits = 0
            status = parts[-1].strip().lower()
            history[code] = {'nombre': name, 'creditos': credits, 'estado': status}
    return history

def check_requirements(student_history, target_curriculum, all_careers, double_career):
    homologables = []
    libre_eleccion = []
    otras_carreras = []
    
    for code, data in student_history.items():
        if data['estado'] != 'aprobado':
            continue
            
        if code in target_curriculum:
            homologables.append({
                'codigo': code,
                'nombre': data['nombre'],
                'creditos': data['creditos'],
                'tipo': 'Homologable'
            })
        else:
            found = False
            for career_name, curriculum in all_careers.items():
                if career_name != double_career and code in curriculum:
                    otras_carreras.append({
                        'codigo': code,
                        'nombre': data['nombre'],
                        'creditos': data['creditos'],
                        'carrera': career_name,
                        'tipo': 'Otra Carrera'
                    })
                    found = True
                    break
            
            if not found:
                libre_eleccion.append({
                    'codigo': code,
                    'nombre': data['nombre'],
                    'creditos': data['creditos'],
                    'tipo': 'Libre Eleccion'
                })
    
    creditos_homologados = sum(c['creditos'] for c in homologables)
    creditos_totales = sum(course['creditos'] for course in target_curriculum.values())
    creditos_faltantes = max(0, creditos_totales - creditos_homologados)
    
    min_creditos = 0.3 * creditos_totales
    cumple_creditos = creditos_homologados >= min_creditos
    cumple_promedio = st.session_state.papa >= 3.8
    
    return {
        'homologables': homologables,
        'otras_carreras': otras_carreras,
        'libre_eleccion': libre_eleccion,
        'creditos_homologados': creditos_homologados,
        'creditos_totales': creditos_totales,
        'creditos_faltantes': creditos_faltantes,
        'cumple_creditos': cumple_creditos,
        'cumple_promedio': cumple_promedio,
        'min_creditos': min_creditos
    }

# ======================
# MALLA CURRICULAR
# ======================
# Matematicas
math_curriculum = """
2015168 fundamentos de matematicas 4 nivelacion
2016377 calculo diferencial en una variable 4 fundamentacion
2025819 introduccion a la teoria de conjuntos 4 disciplinar
2015555 algebra lineal basica 4 fundamentacion
2015556 calculo integral en una variable 4 fundamentacion
2015181 sistemas numericos 4 fundamentacion
2016342 calculo de ecuaciones diferenciales ordinarias 4 disciplinar
2015162 calculo vectorial 4 disciplinar
2015180 programacion y metodos numericos 4 fundamentacion
2015178 probabilidad 4 disciplinar
2015172 geometria elemental 4 disciplinar
1000008 geometria vectorial y analitica 4 disciplinar
2015176 mecanica newtoniana 4 disciplinar
1000017 fundamentos de electricidad y magnetismo 4 disciplinar
2015170 fundamentos de oscilaciones ondas y optica 4 disciplinar
2015167 fundamentos de mecanica de fluidos 3 disciplinar
2015167 fundamentos de fisica moderna 3 disciplinar
2016679 mecanica analitica i 3 disciplinar
2016677 mecanica analitica ii 3 disciplinar
2015173 introduccion a la optimizacion 4 disciplinar
2019082 modelos matematicos 4 disciplinar
2015174 introduccion a la teoria de la computacion 4 disciplinar
2015184 teoria de grafos 4 disciplinar
2015179 procesos estocasticos 4 disciplinar
2015161 analisis estocastico 4 disciplinar
2016834 teoria de conjuntos 1 4 disciplinar
2019092 teoria de modelos 1 4 disciplinar
2025384 epistemologia e historia de la matematica 4 disciplinar
2025580 anillos y modulos 4 disciplinar
2015186 teoria de numeros 4 disciplinar
2019074 ecuaciones diferenciales ordinarias 4 disciplinar
2019075 ecuaciones diferenciales parciales 1 4 disciplinar
2019078 geometria diferencial 1 4 disciplinar
2027312 introduccion al analisis combinatorio 4 disciplinar
2015155 introduccion al analisis real 4 disciplinar
2015153 integracion y series 4 disciplinar
2015151 analisis vectorial 4 disciplinar
2015159 variable compleja 4 disciplinar
2015158 topologia general 4 disciplinar
2015152 grupos y anillos 4 disciplinar
2015149 algebra multilineal y formas canonicas 4 disciplinar
2015157 teoria de cuerpos 4 disciplinar
2015156 logica matematica 4 disciplinar
2019072 analisis numerico 1 4 disciplinar
2015154 trabajo de grado 8 disciplinar
2023605 trabajo de grado asignaturas de posgrado 8 disciplinar
"""

# Estadistica
stats_curriculum = """
2015168 fundamentos de matematicas 4 fundamentacion
2016377 calculo diferencial en una variable 4 fundamentacion
2015181 sistemas numericos 4 fundamentacion
2015556 calculo integral en una variable 4 fundamentacion
2015555 algebra lineal basica 4 fundamentacion
2015162 calculo vectorial 4 fundamentacion
2015178 probabilidad 4 fundamentacion
2015176 mecanica newtoniana 4 disciplinar
2016342 calculo de ecuaciones diferenciales ordinarias 4 disciplinar
2019072 analisis numerico 1 4 disciplinar
2023605 trabajo de grado 8 disciplinar
"""

# Ciencias de la Computacion
cs_curriculum = """
2015168 fundamentos de matematicas 4 fundamentacion
2026573 idioma i 3 fundamentacion
2015181 sistemas numericos 4 fundamentacion
2016377 calculo diferencial en una variable 4 fundamentacion
2015556 calculo integral en una variable 4 fundamentacion
2015555 algebra lineal basica 4 fundamentacion
2025819 introduccion a la teoria de conjuntos 4 disciplinar
2015162 calculo vectorial 4 fundamentacion
2015178 probabilidad 4 disciplinar
2016375 programacion orientada a objetos 3 disciplinar
2015155 introduccion al analisis real 4 disciplinar
2016342 calculo de ecuaciones diferenciales ordinarias 4 disciplinar
2016698 elementos de computador 3 disciplinar
2026555 algebra abstracta y computacional 4 disciplinar
2016699 estructura de datos 3 disciplinar
2016696 algoritmos 3 disciplinar
2015174 introduccion a la teoria de la computacion 4 disciplinar
2016707 sistemas operativos 3 disciplinar
2019072 analisis numerico 1 4 disciplinar
2027633 trabajo de grado 8 disciplinar
"""

# Fisica
physics_curriculum = """
2016650 fundamentos de fisica experimental 3 fundamentacion
2016651 fundamentos de fisica teorica 3 fundamentacion
2016653 taller de matematicas y ciencias 3 fundamentacion
2016377 calculo diferencial en una variable 4 fundamentacion
2015176 mecanica newtoniana 4 disciplinar
2015162 calculo vectorial 4 fundamentacion
2015556 calculo integral en una variable 4 fundamentacion
2016657 electricidad y magnetismo 3 disciplinar
2016342 calculo de ecuaciones diferenciales ordinarias 4 disciplinar
2016686 relatividad 3 disciplinar
2016680 mediciones electromagneticas 3 disciplinar
2016679 mecanica analitica i 3 disciplinar
2016658 oscilaciones y ondas 3 disciplinar
2016693 experimentos en fisica moderna 3 disciplinar
2016677 mecanica analitica ii 3 disciplinar
2016659 electrodinamica i 3 disciplinar
2016681 termodinamica modulo experimental 2 disciplinar
2016691 termodinamica modulo de teoria 2 disciplinar
2016690 mecanica estadistica 3 disciplinar
2016665 electrodinamica ii 3 disciplinar
2016687 mediciones en optica y acustica 3 disciplinar
2016663 introduccion al estado solido 3 disciplinar
2016689 temas de fisica contemporanea 1 disciplinar
2016687 optativa introduccion a la investigacion 3 disciplinar
2016693 optativa aplicaciones de fisica moderna 3 disciplinar
2027633 trabajo de grado 8 disciplinar
"""

# Estructura de carreras
CAREERS = {
    'Matematicas': parse_curriculum(math_curriculum),
    'Fisica': parse_curriculum(physics_curriculum),
    'Estadistica': parse_curriculum(stats_curriculum),
    'Ciencias de la Computacion': parse_curriculum(cs_curriculum)
}

def mostrar():
    # ======================
    # INTERFAZ STREAMLIT
    # ======================

    st.title("🎓 Evaluador de Doble Titulacion - UNAL")
    st.subheader("Facultad de Ciencias - Universidad Nacional de Colombia")

    # Inicializar variables de sesion
    if 'papa' not in st.session_state:
        st.session_state.papa = 4.0
    if 'current_career' not in st.session_state:
        st.session_state.current_career = 'Matematicas'
    if 'double_career' not in st.session_state:
        st.session_state.double_career = 'Fisica'
    if 'results' not in st.session_state:
        st.session_state.results = None

    # Panel de informacion
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona tu carrera actual y la carrera de doble titulacion
        2. Ingresa tu PAPA (Promedio Academico Ponderado Acumulado)
        3. Carga tu historial academico (formato: codigo, nombre, creditos, estado)
        4. El sistema evaluara tu elegibilidad

        Formatos aceptados:
        ```
        Codigo, Nombre, Creditos, Estado
        2015168, Fundamentos de Matematicas, 4, Aprobado
        ```
        o
        ```
        Codigo   Nombre   Creditos   Estado
        2015168   Fundamentos de Matematicas   4   Aprobado
        """)
        st.caption("Nota: Las materias que no pertenecen a ninguna malla del departamento se consideran como libre eleccion")

    # Seleccion de carreras y PAPA
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.session_state.current_career = st.selectbox(
            "Carrera Actual", 
            list(CAREERS.keys()),
            key='current_select'
        )
    with col2:
        available_double = [c for c in list(CAREERS.keys()) if c != st.session_state.current_career]
        st.session_state.double_career = st.selectbox(
            "Carrera de Doble Titulacion", 
            available_double,
            key='double_select'
        )
    with col3:
        st.session_state.papa = st.number_input(
            "PAPA (Promedio Academico Ponderado Acumulado)", 
            min_value=0.0, max_value=5.0, value=4.0, step=0.1
        )

    # Carga de historial academico
    uploaded_file = st.file_uploader("Sube tu historial academico (TXT)", type="txt")

    if uploaded_file:
        student_history_text = uploaded_file.getvalue().decode("utf-8")
        student_history = parse_student_history(student_history_text)
        
        target_career = st.session_state.double_career
        target_curriculum = CAREERS.get(target_career, {})
        
        if target_curriculum:
            st.session_state.results = check_requirements(
                student_history, 
                target_curriculum,
                CAREERS,
                target_career
            )
            
            st.divider()
            st.subheader(f"Resultados para {st.session_state.current_career} a {target_career}")
            
            progress_value = st.session_state.results['creditos_homologados'] / st.session_state.results['creditos_totales']
            st.progress(progress_value)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Creditos Homologados", st.session_state.results['creditos_homologados'])
            col2.metric("Creditos Totales", st.session_state.results['creditos_totales'])
            col3.metric("Creditos Faltantes", st.session_state.results['creditos_faltantes'])
            
            tab1, tab2, tab3 = st.tabs([
                f"Homologables ({len(st.session_state.results['homologables'])})",
                f"Otras Carreras ({len(st.session_state.results['otras_carreras'])})",
                f"Libre Eleccion ({len(st.session_state.results['libre_eleccion'])})"
            ])
            
            with tab1:
                if st.session_state.results['homologables']:
                    for course in st.session_state.results['homologables']:
                        st.write(f"- {course['codigo']}: {course['nombre']} ({course['creditos']} creditos)")
                else:
                    st.write("No se encontraron materias homologables")
                    
            with tab2:
                if st.session_state.results['otras_carreras']:
                    for course in st.session_state.results['otras_carreras']:
                        st.write(f"- {course['codigo']}: {course['nombre']} ({course['creditos']} creditos) -> {course['carrera']}")
                else:
                    st.write("No se encontraron materias de otras carreras")
                    
            with tab3:
                if st.session_state.results['libre_eleccion']:
                    for course in st.session_state.results['libre_eleccion']:
                        st.write(f"- {course['codigo']}: {course['nombre']} ({course['creditos']} creditos)")
                else:
                    st.write("No se encontraron materias de libre eleccion")
            
            st.divider()
            st.subheader("Cumplimiento de Requisitos")
            
            st.write(f"**Creditos minimos (30%):** {'Cumple' if st.session_state.results['cumple_creditos'] else 'No cumple'} (Minimo requerido: {st.session_state.results['min_creditos']:.0f} creditos)")
            st.write(f"**PAPA >= 3.8:** {'Cumple' if st.session_state.results['cumple_promedio'] else 'No cumple'} (Tu PAPA: {st.session_state.papa})")
            
            if st.session_state.results['cumple_creditos'] and st.session_state.results['cumple_promedio']:
                st.success("Cumples con los requisitos para doble titulacion!")
                st.write(f"**Creditos a cursar:** {st.session_state.results['creditos_faltantes']} creditos")
            else:
                st.error("No cumples con los requisitos completos para doble titulacion")
                if not st.session_state.results['cumple_creditos']:
                    st.info(f"Necesitas al menos {st.session_state.results['min_creditos']:.0f} creditos homologables (actuales: {st.session_state.results['creditos_homologados']})")
                if not st.session_state.results['cumple_promedio']:
                    st.info(f"Necesitas PAPA >= 3.8 (actual: {st.session_state.papa})")
        else:
            st.warning(f"La malla curricular para {target_career} no esta disponible")
    else:
        st.info("Por favor carga tu historial academico para comenzar la evaluacion")

    # Footer
    st.divider()
    st.caption("""
    **Notas importantes:**
    1. Este sistema se basa en el Acuerdo 155 de 2014
    2. La decision final depende del Comite Asesor del programa
    3. Requisitos completos: http://www.fcen.unal.edu.co/fileadmin/Reglamento_Doble_Titulacio__n.pdf
    4. Carreras disponibles: Matematicas, Fisica, Estadistica, Ciencias de la Computacion
    """)