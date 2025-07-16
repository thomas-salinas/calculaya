import streamlit as st
from PIL import Image
from pages.opcion_a import main as opcion_a_main
from pages.opcion_b import main as opcion_b_main


if "page" not in st.session_state:
    st.session_state.page = "menu"
if "subpage" not in st.session_state:
    st.session_state.subpage = "inicio"

def show_menu():
    st.markdown("<h1 style='color: #eb4c34;'>Bienvenido a Calulaya</h1>", unsafe_allow_html=True)
    st.subheader("Escoge el tipo de calculadora quieres usar.")
    st.caption("Nota: Presiona dos veces el botón para confirmar")
    st.divider()
    col1, col2 = st.columns(2)
    "\n"


    with col1:
        img1 = Image.open("assets/opcion1.webp")
        if st.button("Académicas", key="btn1"):
            st.session_state.page = "opcion_a"
        st.image(img1, caption="Académico", width = 180)

    with col2:
        img2 = Image.open("assets/opcion2.png")
        if st.button("Personales", key="btn2"):
            st.session_state.page = "opcion_b"
        st.image(img2, caption="Personal", width = 250)


if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "opcion_a":
    opcion_a_main.pagina_principal()
elif st.session_state.page == "opcion_b":
    opcion_b_main.pagina_principal()