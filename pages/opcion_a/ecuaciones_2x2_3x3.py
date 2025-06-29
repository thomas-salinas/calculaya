import streamlit as st
import numpy as np
import pandas as pd
from fractions import Fraction 

def mostrar():
    st.title("Resolver sistema de ecuaciones con 2 o 3 incógnitas")

    # Etiquetas de columnas
    headers = ["x", "y", "z", "i"]

    # Selección de número de ecuaciones
    option = st.selectbox('¿Cuántas ecuaciones quieres resolver?', [2, 3])

    # Mostrar encabezados de la tabla
    cols = st.columns(4)
    for i in range(4):
        cols[i].markdown(f"**{headers[i]}**")

    # Crear inputs según número de ecuaciones
    tabla = []
    for fila in range(option):
        cols = st.columns(4)
        fila_datos = []
        for col in range(4):
            val = cols[col].number_input(f"{headers[col]}{fila+1}", key=f"{fila}-{col}")
            fila_datos.append(val)
        tabla.append(fila_datos)

    # Botón para resolver
    if st.button("Resolver sistema"):
        A = np.array([fila[:option] for fila in tabla])  # matriz de coeficientes
        b = np.array([fila[3] for fila in tabla])         # vector independientes

        # Mostrar sistema ingresado en LaTeX
        st.latex(r"""\text{Sistema de ecuaciones:}""")
        for i in range(option):
            ecuacion = " + ".join([f"{tabla[i][j]}{headers[j]}" for j in range(option)])
            st.latex(f"{ecuacion} = {tabla[i][3]}")

        # Resolver sistema
        try:
            sol = np.linalg.solve(A, b)

            # Convertir a fracciones
            fracciones = [Fraction(x).limit_denominator() for x in sol]

            # Mostrar solución en fracciones
            st.success("✅ Solución encontrada:")
            resultado_frac = ",\\quad ".join([
                f"{headers[i]} = \\frac{{{fracciones[i].numerator}}}{{{fracciones[i].denominator}}}"
                if fracciones[i].denominator != 1 else f"{headers[i]} = {fracciones[i].numerator}"
                for i in range(option)
            ])
            st.latex(resultado_frac)

        except np.linalg.LinAlgError:
            st.error("❌ El sistema no tiene solución única (es incompatible o tiene infinitas soluciones).")
