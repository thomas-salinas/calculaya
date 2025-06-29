import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def mostrar():
    st.title("Interpolación de Lagrange")
    st.write("Este programa construye el polinomio interpolador de Lagrange a partir de puntos dados.")

    n = st.number_input("¿Cuántos puntos vas a ingresar?", min_value = 2, step = 1)

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
        st.write(f"P({x_eval}) = {resultado}")

    if st.checkbox("Mostrar gráfico"):
        fx = sp.lambdify(x, P_simplificado, 'numpy')
        x_vals = np.linspace(min(xi) - 1, max(xi) + 1, 500)
        y_vals = fx(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label="Polinomio de Lagrange")
        ax.plot(xi, yi, 'ro', label="Puntos dados")
        ax.set_title("Interpolación de Lagrange")
        ax.set_xlabel("x")
        ax.set_ylabel("P(x)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)
