import requests
import json
import streamlit as st
import time


def moedas():
    cotação = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-USD,USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-BRL")
    cotações = cotação.json()

    st.title('Conversor de Moedas')
    moeda_input = st.selectbox('DE:', ['USD', 'EUR', 'BRL'])
    moeda_output = st.selectbox('PARA:', ['USD', 'EUR', 'BRL'])

    if moeda_input == 'USD':
        if moeda_output == 'BRL':
            valor = st.number_input('Informe o valor desejado', 0.0)
            dolar = float(cotações["USDBRL"]["bid"])
            resultado = dolar * valor
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success("{:.2f}USD é equivalente à {:.2f}BRL".format(valor, resultado))
        elif moeda_output == 'EUR':
            valor = st.number_input('Informe o valor desejado', 0.0)
            dolar_euro = float(cotações['USDEUR']['bid'])
            resultado = dolar_euro * valor
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success("{:.2f}USD é equivalente à {:.2f}EUR".format(valor, resultado ))
        elif moeda_output == 'USD':
            valor = st.number_input('Informe o valor desejado', 0.0)
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success('{:.2f}USD é equivalente à {:.2f}USD'.format(valor, valor))

    elif moeda_input == 'BRL':
        if moeda_output == 'USD':
            real_dolar = (float(cotações['BRLUSD']['bid']))
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            resultado2 = real_dolar * valor2
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success('{:.2f}BRL é equivalente à {:.2f}USD'.format(valor2, resultado2))
        elif moeda_output == 'EUR':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            real_euro = (float(cotações['BRLEUR']['bid']))
            resultado2 = real_euro * valor2
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success('{:.2f}BRL é equivalente à {:.2f}EUR'.format(valor2, resultado2))
        elif moeda_output == 'BRL':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('')
                st.write('Prontinho!')
                st.success('{:.2f}BRL é equivalente à {:.2f}BRL'.format(valor2, valor2))

    elif moeda_input == 'EUR':
        if moeda_output == 'BRL':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            euro_real = (float(cotações['USDBRL']['bid']))
            resultado2 = euro_real * valor2
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success('{:.2f}EUR é equivalente à {:.2f}BRL'.format(valor2, resultado2))
        elif moeda_output == 'USD':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            euro_dol = (float(cotações['EURUSD']['bid']))
            resultado2 = euro_dol * valor2
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('Prontinho!')
                st.success('{:.2f}EUR equivalente à {:.2f}USD'.format(valor2, resultado2))
        elif moeda_output == 'EUR':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            if st.button('CONVERTER'):
                st.write('Aguarde um instante, estamos convertendo..')
                time.sleep(1)
                st.write('')
                st.write('Prontinho!')
                st.success('{:.2f}EUR é equivalente à {:.2f}EUR'.format(valor2, valor2))