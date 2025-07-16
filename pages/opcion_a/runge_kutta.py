import streamlit as st
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def runge_Kutta_4(f, y0, x0, xf, h):
    n = int((xf - x0) / h) + 1
    x = np.linspace(x0, xf, n)
    y = np.zeros(n)
    y[0] = y0

    for i in range(n - 1):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x, y

# EDO específica
def f(x, y):
    return math.exp(-x * y)

# Función principal en Streamlit
def mostrar():
    st.title("Método de Runge-Kutta de 4to Orden")
    st.write("Esta calculadora implementa el método de Runge-Kutta de cuarto orden para aproximar la solución de una ecuación diferencial ordinaria (EDO) de la forma $\\frac{dy}{dx} = f(x, y)$, dada una condición inicial.")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
            1. Ingresa los valores iniciales, el valor final y el tamaño del paso.
            2. Presiona el botón "Calcular" para ver la tabla y la gráfica.
        """)
    st.divider()

    st.write("Se resuelve la siguiente ecuación diferencial:")
    st.latex(r"\frac{dy}{dx} = e^{-xy}")

    with st.form("rk4_form"):
        y0 = st.number_input("Valor inicial de $y$ cuando $x = 0$", value=1.0, format="%.4f")
        x0 = st.number_input("Valor inicial de $x$ ($x_0$)", value=0.0, format="%.4f")
        xf = st.number_input("Valor final de $x$ ($x_f$)", value=2.0, format="%.4f")
        h = st.number_input("Tamaño del paso ($h$)", min_value=0.001, value=0.1, step=0.001, format="%.4f")
        submitted = st.form_submit_button("Calcular")

    if submitted:
        x, y = runge_Kutta_4(f, y0, x0, xf, h)

        st.subheader("📋 Tabla de resultados")
        df = pd.DataFrame({"x": x, "y": y})
        st.dataframe(df.style.format({"x": "{:.4f}", "y": "{:.6f}"}))

        st.subheader("📈 Gráfica de la solución")
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', color='blue', linestyle='-')
        ax.set_xlabel("x")
        ax.set_ylabel("y(x)")
        ax.set_title("Solución aproximada con Runge-Kutta 4")
        ax.grid(True)
        st.pyplot(fig)
