import streamlit as st

def euler(f, x0, y0, h, n):
    results = [(x0, y0)]
    x, y = x0, y0
    for i in range(n):
        y += h * f(x, y)
        x += h
        results.append((x, y))
    return results

def mostrar():
    st.title("Método de Euler para EDOs")

    st.markdown("La ecuación debe tener la forma $\\frac{dy}{dx} = f(x, y)$")
    
    # Entrada para la función
    func_str = st.text_input("Ingresa la función f(x, y):", value="x + y")
    
    # Validación rápida de función
    try:
        f = eval(f"lambda x, y: {func_str}")
        f(1, 1)  # test rápido
        funcion_valida = True
    except Exception as e:
        st.error(f"Error en la función ingresada: {e}")
        funcion_valida = False

    # Entradas numéricas
    x0 = st.number_input("Valor inicial de x (x₀):", value=0.0)
    y0 = st.number_input("Valor inicial de y (y₀):", value=1.0)
    h = st.number_input("Tamaño de paso (h):", value=0.1)
    n = st.number_input("Número de pasos (n):", value=10, step=1)

    if funcion_valida and st.button("Calcular"):
        resultado = euler(f, x0, y0, h, int(n))
        
        st.success("Resultados:")
        for i, (x, y) in enumerate(resultado):
            st.write(f"Paso {i}: x = {x:.5f}, y ≈ {y:.5f}")
