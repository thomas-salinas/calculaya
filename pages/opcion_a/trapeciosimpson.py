import streamlit as st
import sympy as sp
import numpy as np
import re

def mostrar():
    st.title("🧮 Regla del Trapecio Compuesta")
    
    st.write("Calculadora para aproximar integrales con la regla del trapecio compuesta.")
    with st.expander("Instrucciones de Uso", expanded=True):
        st.write("""
        1. Ingresa la función usando notación matemática simple.
        2. Usa `x2` para representar x al cuadrado (se convertirá a `x**2` automáticamente).
        3. Presiona el botón "Calcular" para ver los resultados.
        """)
    st.divider()

    x = sp.Symbol('x')

    funcion_str = st.text_input("Introduce la función f(x) a integrar:", value="x2 + 1")
    st.caption("Usa `x2` para x al cuadrado, `x3` para x al cubo, etc.")

    # Reemplazar potencias estilo x2 por x**2
    funcion_str_modificada = re.sub(r'([a-zA-Z])(\d+)', r'\1**\2', funcion_str)

    try:
        funcion = sp.sympify(funcion_str_modificada)
        f_num = sp.lambdify(x, funcion, 'numpy')
        funcion_valida = True
    except Exception as e:
        st.error(f"La función no es válida: {e}")
        funcion_valida = False

    a = st.number_input("Límite inferior de integración (a):", value=0.0)
    b = st.number_input("Límite superior de integración (b):", value=1.0)
    n = st.number_input("Número de subintervalos (n):", min_value=1, step=1, value=4)

    if funcion_valida and st.button("Calcular integral"):
        h = (b - a) / n
        st.write(f"Tamaño de cada subintervalo (h): {h:.6f}")

        puntos_x = np.linspace(a, b, n + 1)
        try:
            valores_y = f_num(puntos_x)
        except Exception as e:
            st.error(f"Error al evaluar la función: {e}")
            return

        st.subheader("Puntos de evaluación:")
        for i, (xi, yi) in enumerate(zip(puntos_x, valores_y)):
            xi_str = f"{xi:.6f}"
            yi_str = f"{yi:.6f}"
            st.latex(f"x_{{{i}}} = {xi_str},\\quad f(x_{{{i}}}) = {yi_str}")

        suma_total = valores_y[0] + valores_y[-1] + 2 * sum(valores_y[1:-1])
        integral_aproximada = (h / 2) * suma_total

        st.success("Resultado de la integral aproximada:")
        st.latex(f"\\int_{{{a}}}^{{{b}}} f(x)\\,dx \\approx {integral_aproximada:.10f}")
