import streamlit as st
import sympy as sp
import numpy as np
import re

def mostrar():
    st.title("Método de Newton-Raphson para sistemas no lineales")
    st.write("Calculadora para resolver sistemas de 2 ecuaciones no lineales con 2 incógnitas.")

    with st.expander("Instrucciones de Uso", expanded=True):
        st.markdown("""
**1.** Ingresa las funciones en términos de $x$ y $y$.  
**2.** Puedes escribir potencias como `x2` en vez de `x**2`, `y3` en vez de `y**3`, etc.  
**3.** Presiona el botón **"Calcular solución"** para iniciar el proceso iterativo.
""")

    st.divider()

    st.markdown("### 🧮 Ingreso de funciones")

    # Definir variables simbólicas
    x, y = sp.symbols('x y')

    f1_str = st.text_input("**Primera función –** $f_1(x, y)$:", "x2 + y2 - 4")
    f2_str = st.text_input("**Segunda función –** $f_2(x, y)$", "x*y - 1")

    # Reemplazar x2 -> x**2, y3 -> y**3, etc.
    def convertir_potencias(expr_str):
        return re.sub(r'([a-zA-Z])(\d+)', r'\1**\2', expr_str)

    f1_str_mod = convertir_potencias(f1_str)
    f2_str_mod = convertir_potencias(f2_str)

    try:
        f1 = sp.sympify(f1_str_mod)
        f2 = sp.sympify(f2_str_mod)
    except Exception as e:
        st.error(f"Error en la expresión: {e}")
        return

    # Mostrar funciones parseadas en LaTeX
    st.markdown("### 📄 Funciones interpretadas:")
    st.latex(r"f_1(x, y) = " + sp.latex(f1))
    st.latex(r"f_2(x, y) = " + sp.latex(f2))

    # Construcción simbólica
    F = sp.Matrix([f1, f2])
    vars = sp.Matrix([x, y])
    J = F.jacobian(vars)
    F_lambdified = sp.lambdify((x, y), F, 'numpy')
    J_lambdified = sp.lambdify((x, y), J, 'numpy')

    # Parámetros numéricos
    st.markdown("### ⚙️ Parámetros del método")
    x0 = st.number_input("Valor inicial para \( x_0 \)", value=1.0, format="%.6f")
    y0 = st.number_input("Valor inicial para \( y_0 \)", value=1.0, format="%.6f")
    tol = st.number_input("Tolerancia", value=1e-6, format="%.1e")
    max_iter = st.number_input("Máximo número de iteraciones", min_value=1, value=20)

    if st.button("Calcular solución"):
        resultados = []

        for i in range(1, max_iter + 1):
            F_val = np.array(F_lambdified(x0, y0), dtype=float).flatten()
            J_val = np.array(J_lambdified(x0, y0), dtype=float)

            try:
                delta = np.linalg.solve(J_val, -F_val)
            except np.linalg.LinAlgError:
                st.error(f"Jacobiana singular en la iteración {i}. Detenido.")
                break

            x1 = x0 + delta[0]
            y1 = y0 + delta[1]
            error = np.linalg.norm([x1 - x0, y1 - y0])

            resultados.append((i, x1, y1, error))

            if error < tol:
                st.success("✅ Solución encontrada:")
                st.latex(f"x = {x1:.6f}, \quad y = {y1:.6f}")
                break

            x0, y0 = x1, y1
        else:
            st.warning("⚠️ No se alcanzó la convergencia en el número máximo de iteraciones.")

        # Mostrar tabla
        st.subheader("📋 Tabla de iteraciones")
        st.table([
            {"Iteración": i, "x": f"{x1:.6f}", "y": f"{y1:.6f}", "Error": f"{err:.2e}"}
            for i, x1, y1, err in resultados
        ])
