import streamlit as st
from PIL import Image
from pages.opcion_a import main as opcion_a_main
from pages.opcion_b import main as opcion_b_main


if "page" not in st.session_state:
    st.session_state.page = "menu"
if "subpage" not in st.session_state:
    st.session_state.subpage = "inicio"

def show_menu():
    st.title("Elige una opción")
    col1, col2 = st.columns(2)

    with col1:
        img1 = Image.open("assets/opcion1.webp")
        if st.button("Opción A", key="btn1"):
            st.session_state.page = "opcion_a"
        st.image(img1, caption="Académico")

    with col2:
        img2 = Image.open("assets/opcion2.png")
        if st.button("Opción B", key="btn2"):
            st.session_state.page = "opcion_b"
        st.image(img2, caption="Personal")


if st.session_state.page == "menu":
    show_menu()
elif st.session_state.page == "opcion_a":
    opcion_a_main.pagina_principal()
elif st.session_state.page == "opcion_b":
    opcion_b_main.pagina_principal()
