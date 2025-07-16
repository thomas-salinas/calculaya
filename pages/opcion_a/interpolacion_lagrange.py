import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def mostrar():
    st.title("🧮 Interpolación de Lagrange")
    st.write("Este programa construye el polinomio interpolador de Lagrange a partir de puntos dados.")
    st.write("\n")
    
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Ingresa los datos solicitados.
        2. Marca la casilla "Evaluar el polinomio en un punto" para obtener valores.
        3. Si los datos son válidos, se habilitará la opción para graficar.
        """)
    
    st.divider()
    n = st.number_input("¿Cuántos puntos vas a ingresar?", min_value=2, step=1)

    xi = []
    yi = []

    st.subheader("Ingresa los puntos (x, y):")
    for i in range(n):
        col1, col2 = st.columns(2)
        with col1:
            x_val = st.number_input(f"x[{i}]", key=f"x_{i}")
        with col2:
            y_val = st.number_input(f"y[{i}]", key=f"y_{i}")
        xi.append(x_val)
        yi.append(y_val)

    # Validar si hay datos completos y x únicos
    datos_completos = all([not np.isnan(xi[i]) and not np.isnan(yi[i]) for i in range(n)])
    x_unicos = len(set(xi)) == len(xi)

    if not datos_completos:
        st.warning("Por favor, completa todos los valores de x e y.")
        return
    if not x_unicos:
        st.error("Los valores de x deben ser únicos para evitar divisiones por cero.")
        return

    # Cálculo del polinomio
    x = sp.Symbol('x')
    P = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - xi[j]) / (xi[i] - xi[j])
        P += yi[i] * L

    P_simplificado = sp.simplify(P)

    st.subheader("Polinomio de interpolación:")
    st.latex(f"P(x) = {sp.latex(P_simplificado)}")

    if st.checkbox("Evaluar el polinomio en un punto"):
        x_eval = st.number_input("Introduce el valor de x para evaluar:")
        resultado = P_simplificado.subs(x, x_eval)
        st.latex(f"P({sp.latex(x_eval)}) = {sp.latex(resultado)}")

    if datos_completos and x_unicos:
        if st.checkbox("Mostrar gráfico"):
            try:
                fx = sp.lambdify(x, P_simplificado, 'numpy')
                x_vals = np.linspace(min(xi) - 1, max(xi) + 1, 500)
                y_vals = fx(x_vals)

                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, label="Polinomio de Lagrange", color="blue")
                ax.plot(xi, yi, 'ro', label="Puntos dados")
                ax.set_title("Interpolación de Lagrange")
                ax.set_xlabel("x")
                ax.set_ylabel("P(x)")
                ax.grid(True)
                ax.legend()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Error al graficar: {str(e)}")
