import streamlit as st


def raiz():
    st.title('Raiz Quadrada')
    num1 = (st.number_input('Informe o número que deseja descobrir a raiz quadrada', 0))
    if st.button("Converter"):
        st.success('A raiz quadrada de {} é {:.2f}'.format(num1, num1 ** (1/2)))