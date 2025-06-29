import streamlit as st
import sympy as sp
import numpy as np

def mostrar():
    st.title("Regla del Trapecio Compuesta")

    # Paso 1: Definir símbolo
    x = sp.Symbol('x')

    # Paso 2: Entrada de la función
    funcion_str = st.text_input("Introduce la función f(x) a integrar:", value="x**2 + 1")

    try:
        funcion = sp.sympify(funcion_str)
        f_num = sp.lambdify(x, funcion, 'numpy')
        funcion_valida = True
    except Exception as e:
        st.error(f"La función no es válida: {e}")
        funcion_valida = False

    # Paso 3: Límites
    a = st.number_input("Límite inferior de integración (a):", value=0.0)
    b = st.number_input("Límite superior de integración (b):", value=1.0)

    # Paso 4: Número de subintervalos
    n = st.number_input("Número de subintervalos (n):", min_value=1, step=1, value=4)

    # Botón para calcular
    if funcion_valida and st.button("Calcular integral"):
        # Paso 5: Tamaño de subintervalo
        h = (b - a) / n
        st.write(f"Tamaño de cada subintervalo (h): {h:.6f}")

        # Paso 6-7: Evaluar puntos
        puntos_x = np.linspace(a, b, n + 1)
        try:
            valores_y = f_num(puntos_x)
        except Exception as e:
            st.error(f"Error al evaluar la función: {e}")
            return

        # Mostrar tabla de evaluación
        st.subheader("Puntos de evaluación:")
        for i, (xi, yi) in enumerate(zip(puntos_x, valores_y)):
            st.write(f"x{i} = {xi:.6f}   f(x{i}) = {yi:.6f}")

        # Paso 8: Regla del trapecio compuesta
        suma_total = valores_y[0] + valores_y[-1] + 2 * sum(valores_y[1:-1])
        integral_aproximada = (h / 2) * suma_total

        st.success(f"Resultado de la integral aproximada: {integral_aproximada:.10f}")
