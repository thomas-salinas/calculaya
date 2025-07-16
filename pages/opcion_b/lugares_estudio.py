import streamlit as st
import math

Comedores = {'Comedor Central': (555.961, -556.373), 'Comedor de Derecho y Ciencias Políticas': (481.172, -532.167), 'Comedor Yu Takeuchi': (510.033, -392.209), 'Comedor Geología': (429.037, -670.884), 'Comedor Economía': (626.096, -389.726), 'Comedor Agrarias': (275.424, -573.441), 'Comedor Odontología': (420.658, -606.025), 'Comedor Biologia': (502.895, -222.148), 'Comedor Hemeroteca': (71.358, -603.432), 'Comedor Aulas de Humanas': (450.575, -635.408)}

Edificios = {'Portería 30': (700.764, -503.506), 'Edificio Ciencia y Tecnología (CyT)': (384.5, -415.072), 'Auditorio León de Greiff': (569.112, -498.51), 'Biblioteca Central (Gabriel García Márquez)': (524.645, -531.985), 'Sala Central de Cómputo': (580.604, -550.971), 'Portería Calle 26': (528.143, -699.361), 'Edificio Posgrados de Ciencias Humanas': (355.271, -659.39), 'Edificio Aulas de Humanas': (458.195, -629.413), 'Edificio Manuel Ancízar': (420.223, -665.386), 'Edificio de Filosofía': (571.985, -684.622), 'Edificio de Enfermería': (427.093, -558.465), 'Edificio de Lenguas Extranjeras': (491.045, -674.879), 'Edificio Antonio Nariño (Lingüística- Ing, Civil y Agrícola)': (510.531, -638.906), 'Diseño Gráfico': (562.492, -636.907), 'Edificio de Posgrado de Ciencias Económicas': (598.465, -617.921), 'Edificio de Derecho y Ciencias políticas': (491.045, -545.475), 'Portería Capilla': (694.394, -588.443), 'Edificio de Ciencias Agrarias': (279.703, -565.96), 'Química': (449.576, -414.572), 'Aulas de Ingeniería': (436.086, -368.357), 'Portería Calle 53': (382.626, -63.334), 'Genética': (411.105, -132.532), 'Portería Carrera 45': (113.326, -402.332), 'Portería Hemeroteca': (72.607, -651.646), 'Estadio Alfonso López Pumarejo': (247.477, -316.895), 'Ciencias Económicas': (616.452, -380.348), 'Hemeroteca Nacional': (59.866, -601.933), 'NEA': (587.599, -420.568), 'Edificio Yu Takeuchi Matemáticas y Física': (524.895, -383.596), 'Posgrados de Matemáticas y Física': (567.613, -374.852), 'Edificio Julio Garavito ("El viejo" de Ingeniería)': (504.91, -423.316), 'SINDU': (663.292, -452.294), 'Edificio Gloria Galeano': (275.081, -515.248), 'Facultad de Ciencias': (360.517, -461.787), 'Medicina': (443.955, -494.763), 'Farmacia': (451.949, -443.801), 'Sociología': (501.288, -587.444), 'Odonotología': (409.856, -607.429), 'Facultad de Medicina Veterinaria y de Zootécnia': (387.123, -525.365), 'Instituto de Ciencias Naturales': (474.932, -145.023), 'Laboratorios de Ing. Mecánica y Eléctrica': (482.427, -324.889), 'Laboratorios de Ingeniería Química': (464.94, -347.872), 'Biología': (501.163, -198.233)}

Lugares_estudio_silencioso={'Sala de Cómputo de Historia': (420.223, -665.386),'Biblioteca de Género': (420.223, -665.386),'Sala de Cómputo de Filosofía': (571.985, -684.622),'Biblioteca de Posgrados de Ciencias Humanas': (355.271, -659.39),'Hemeroteca Nacional': (59.866, -601.933),'Cuarto piso Biblioteca Central (Gabriel García Márquez)': (524.645, -531.985),'Biblioteca de Lenguas Extranjeras': (491.045, -674.879)}
Lugares_estudio_grupo={'Biblioteca de Género': (420.223, -665.386),'Hemeroteca Nacional': (59.866, -601.933),'Biblioteca Central (Gabriel García Márquez)': (524.645, -531.985),'Biblioteca de Lenguas Extranjeras': (491.045, -674.879),'NEA': (587.599, -420.568), 'Sala Jaime Jaramillo Uribe': (420.223, -665.386),'Biblioteca Economía': (616.452, -380.348),'Biblioteca del edificio de Ciencia y Tecnología (CyT)': (384.5, -415.072),'Sala Central de Cómputo': (580.604, -550.971),'Sala de estudio de Matemáticas': (524.895, -383.596), 'Biblioteca de Ciencias Agrarias': (279.703, -565.96),'Biblioteca de Medicina Veterinaria y de Zootécnia': (387.123, -525.365),'Sala de Cómputo Aulas de Humanas': (458.195, -629.413),'Sala de estudio de Ingeniería': (504.91, -423.316),'Sala de estudio de Química': (449.576, -414.572),'Sala de estudio de Agronomía': (279.703, -565.96)}
Lugares_estudio_lonelly_no_case ={'Biblioteca de Género': (420.223, -665.386),'Hemeroteca Nacional': (59.866, -601.933),'Biblioteca Central (Gabriel García Márquez)': (524.645, -531.985),'Biblioteca de Lenguas Extranjeras': (491.045, -674.879),'NEA': (587.599, -420.568), 'Sala Jaime Jaramillo Uribe': (420.223, -665.386),'Biblioteca Economía': (616.452, -380.348),'Biblioteca del edificio de Ciencia y Tecnología (CyT)': (384.5, -415.072),'Sala Central de Cómputo': (580.604, -550.971),'Sala de estudio de Matemáticas': (524.895, -383.596), 'Biblioteca de Ciencias Agrarias': (279.703, -565.96),'Biblioteca de Medicina Veterinaria y de Zootécnia': (387.123, -525.365),'Sala de Cómputo Aulas de Humanas': (458.195, -629.413),'Sala de estudio de Ingeniería': (504.91, -423.316),'Sala de estudio de Química': (449.576, -414.572),'Sala de estudio de Agronomía': (279.703, -565.96),'Sala de Cómputo de Historia': (420.223, -665.386),'Sala de Cómputo de Filosofía': (571.985, -684.622),'Biblioteca de Posgrados de Ciencias Humanas': (355.271, -659.39),'Biblioteca de Lenguas Extranjeras': (491.045, -674.879)}

def mostrar():
    st.title("✍️ Lugares de estudio en la UNAL")
    st.write("Herramienta para consultar qué lugares de estudio existen en la UNAL - sede Bogotá")
    st.write("\n")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Selecciona si deseas estudiar en grupo o solo.
        2. Si estudias solo, marca si quieres que el lugar sea silencioso o no.
        2. Selecciona en qué edificio estás.
        3. Presiona el botón "Buscar" para ver los resultados.
        """)
    st.divider()

    # Options to choose. Take into account that options to choose are with the dictionaries
    study_mode = st.radio("¿Cómo deseas estudiar?", ("En grupo 👥 ", "Solo 👤"))
    quiet_place = None
    if study_mode == "Solo 👤":
        quiet_place = st.radio("🔇 ¿Deseas estudiar en un lugar silencioso?:", ("Sí", "No"))
    opcion = st.selectbox("🏢 ¿En cuál edificio estás?", list(Edificios.keys()))
    
    

    if st.button("Buscar"):
       
        x0, y0 = Edificios[opcion]
        min_comedor = None
        min_dist = float("inf")

        
        #Same logic as George's code
        if study_mode == "En grupo 👥":
            for nombre, (x, y) in Lugares_estudio_grupo.items():
                dist = math.hypot(x - x0, y - y0)
                if dist < min_dist:
                    min_dist = dist
                    min_comedor = nombre
        #Option when user want to study in quiet place.
        elif quiet_place =="Sí":
            for nombre, (x, y) in Lugares_estudio_silencioso.items():
                dist = math.hypot(x - x0, y - y0)
                if dist < min_dist:
                    min_dist = dist
                    min_comedor = nombre
        else:
            for nombre, (x, y) in Lugares_estudio_lonelly_no_case.items():
                dist = math.hypot(x - x0, y - y0)
                if dist < min_dist:
                    min_dist = dist
                    min_comedor = nombre

        st.success(f"El lugar de estudio más cercano que responde a sus necesidades es: **{min_comedor}**")
        st.info("Recuerda siempre tomar un descanso ;)")

    with st.expander("Mapa UNAL - Sede Bogotá", expanded=True):
        st.image("assets/maps.png", caption="Mapa UNAL Bogotá")