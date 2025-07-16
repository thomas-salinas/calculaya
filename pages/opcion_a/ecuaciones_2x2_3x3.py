import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def mostrar():
    st.title("🧮 Resolver sistema 2x2 y mostrar gráfico")
    st.write("Calculadora para resolver sistemas de 2 ecuaciones lineales con 2 incógnitas.")
    
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Ingresa los coeficientes de las ecuaciones (forma: ax + by = c).
        2. Presiona 'Resolver sistema' para ver el resultado y su gráfico.
        """)
    st.divider()

    headers = ["x", "y", "término independiente"]

    # Entradas de datos
    tabla = []
    for i in range(2):
        cols = st.columns(3)
        fila = []
        for j in range(3):
            val = cols[j].number_input(f"{headers[j]}{i+1}", key=f"{i}-{j}")
            fila.append(val)
        tabla.append(fila)

    if st.button("Resolver sistema"):
        A = np.array([fila[:2] for fila in tabla])
        b = np.array([fila[2] for fila in tabla])

        # Mostrar sistema ingresado
        st.latex(r"\text{Sistema de ecuaciones:}")
        for i in range(2):
            ecuacion = f"{tabla[i][0]}x + {tabla[i][1]}y = {tabla[i][2]}"
            st.latex(ecuacion)

        det_A = np.linalg.det(A)

        # Clasificación del sistema
        if det_A != 0:
            # Solución única
            sol = np.linalg.solve(A, b)
            fracciones = [Fraction(s).limit_denominator() for s in sol]

            st.success("✅ El sistema tiene solución única:")
            latex_sol = ",\\quad ".join([
                f"x = \\frac{{{fracciones[0].numerator}}}{{{fracciones[0].denominator}}}" if fracciones[0].denominator != 1 else f"x = {fracciones[0].numerator}",
                f"y = \\frac{{{fracciones[1].numerator}}}{{{fracciones[1].denominator}}}" if fracciones[1].denominator != 1 else f"y = {fracciones[1].numerator}"
            ])
            st.latex(latex_sol)
        else:
            # Determinante 0: revisar compatibilidad
            A_ext = np.column_stack((A, b))
            rango_A = np.linalg.matrix_rank(A)
            rango_ext = np.linalg.matrix_rank(A_ext)

            if rango_A == rango_ext:
                st.warning("♾️ El sistema tiene infinitas soluciones (es compatible indeterminado).")
            else:
                st.error("❌ El sistema no tiene solución (es incompatible).")

        # Mostrar gráfico
        st.subheader("📈 Representación gráfica")

        x_vals = np.linspace(-10, 10, 500)
        colores = ['blue', 'green']
        etiquetas = ['Ecuación 1', 'Ecuación 2']

        fig, ax = plt.subplots()
        for i in range(2):
            a, b_, c = tabla[i]
            if b_ != 0:
                y_vals = (c - a * x_vals) / b_
                ax.plot(x_vals, y_vals, label=etiquetas[i], color=colores[i])
            elif a != 0:
                x_recta = c / a
                ax.axvline(x=x_recta, label=etiquetas[i], color=colores[i])

        # Si tiene solución única, marcar punto de intersección
        if det_A != 0:
            ax.plot(sol[0], sol[1], 'ro', label="Intersección")

        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        ax.set_title("Sistema de ecuaciones")

        st.pyplot(fig)
