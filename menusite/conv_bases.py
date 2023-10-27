import streamlit as st
import time

def bases():

    st.title('Conversor de bases númericas')
    base_input = st.selectbox('De:', ['BINÁRIO', 'DECIMAL', 'HEXADECIMAL', 'OCTAL'])
    base_output = st.selectbox('Para:', ['BINÁRIO', 'DECIMAL', 'HEXADECIMAL', 'OCTAL'])

    if base_input == 'DECIMAL':
        if base_output == 'BINÁRIO':
            st.write('')
            st.write('')
            base_number = st.number_input('Informe o número que deseja converter', 0)
            st.write('')
            st.success(bin(base_number)[2:])
        elif base_output == 'DECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            st.write('')
            st.write('')
            st.success(base_number)
        elif base_output == 'HEXADECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            st.write('')
            st.write('')
            st.success(hex(base_number)[2:].upper())
        elif base_output == 'OCTAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            st.write('')
            st.write('')
            st.success(oct(base_number)[2:])

    elif base_input == 'BINÁRIO':
        if base_output == 'DECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(base_number))
            valor_digitado = base_number
            decimal = 0
            i = 0
            while n >= 0:
                resto = base_number % 10
                decimal = decimal + (resto * (2 ** i))
                n = n - 1
                i = i + 1
                base_number = base_number // 10
            st.write('')
            st.write('')
            st.success(decimal)
        elif base_output == 'HEXADECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(base_number))
            valor_digitado = base_number
            decimal = 0
            i = 0
            while n >= 0:
                resto = base_number % 10
                decimal = decimal + (resto * (2 ** i))
                n = n - 1
                i = i + 1
                base_number = base_number // 10
            st.write('')
            st.write('')
            st.success(hex(decimal)[2:].upper())

        elif base_output == 'OCTAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(base_number))
            valor_digitado = base_number
            decimal = 0
            i = 0
            while n >= 0:
                resto = base_number % 10
                decimal = decimal + (resto * (2 ** i))
                n = n - 1
                i = i + 1
                base_number = base_number // 10
            st.write('')
            st.write('')
            st.success(oct(decimal)[2:])

        elif base_output == 'BINÁRIO':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(bin(base_number)))
            st.write('')
            st.write('')
            st.success(base_number)

    elif base_input == 'HEXADECIMAL':
        if base_output == 'BINÁRIO':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 16)
            binario = bin(decimal)
            st.success(binario[2:])
        if base_output == 'DECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 16)
            st.success(decimal)
        if base_output == 'OCTAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 16)
            octal = oct(decimal)
            st.success(octal[2:])
        if base_output == 'HEXADECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            st.success(base_number)
    else:
        if base_output == 'BINÁRIO':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 8)
            binario = bin(decimal)
            st.success(binario[2:])

        elif base_output == 'DECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 8)
            st.success(decimal)
        elif base_output == 'HEXADECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 8)
            binario = hex(decimal)
            st.success(binario[2:].upper())
        else:
            base_number = st.number_input('Informe o número que deseja converter', 0)
            st.success(base_number)
