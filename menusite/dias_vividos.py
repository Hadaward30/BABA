import streamlit as st
import datetime as dt

def dias_vividos():
    def calcular_dias_de_vida(data_nascimento):
        hoje = dt.datetime.today()
        data_nascimento = dt.datetime.strptime(data_nascimento, "%Y-%m-%d")
        dias_de_vida = (hoje - data_nascimento).days
        return dias_de_vida

    st.title('Calculando dias vividos')
    data_nascimento = st.date_input('Digite sua data de nascimento')

    if st.button('Calcular dias de vida'):
        dias_de_vida = calcular_dias_de_vida(str(data_nascimento))
        st.write('')
        st.write('')
        st.write('')
        st.success(f'Você viveu {dias_de_vida} dias até agora!')


