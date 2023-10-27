
import streamlit as st
import menusite.dias_vividos as d_vividos
import menusite.raiz_quadrada as r_quadrada
import menusite.conv_moedas as c_moed
import menusite.conv_bases as bases_num



st.set_page_config("RemaKing")

page_bg_img = f"""

<style>
[data-testid ="stAppViewContainer"] {{
background-image: url("https://a.imagem.app/bU1DmS.png");
background-size: cover;
font-size: 16px;
 }}
 
[data-testid="stSidebar"] {{
background-color: rgba(35,30,63,0.5);
}}
[data-testid="stHeader"] {{
background-color: rgba(30,57,63,0.0);
}}
[data-testid="stDecoration"] {{
height: 0rem;
}}
footer {{
visibility: hidden;
}}


</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.title('Menu')
paginaselecionada = st.sidebar.selectbox('Selecione a ferramenta que deseja', ['--', 'Raiz quadrada','Conversão de bases', 'Dias Vividos', 'Conversão de Moedas', 'Conversão de temperatura'])

if paginaselecionada == '--':
     st.write('')

elif paginaselecionada == 'Dias Vividos':
    page_bg_imge = f"""
            <style>
        [data-testid ="stAppViewContainer"] {{
        background-image: url(https://a.imagem.app/batHpt.png);
        background-size: cover;
        font-size: 16px;
         }}


        </style>
        """
    st.markdown(page_bg_imge, unsafe_allow_html=True)
    d_vividos.dias_vividos()

elif paginaselecionada == 'Raiz quadrada':
    page_bg_imge = f"""
                <style>
            [data-testid ="stAppViewContainer"] {{
            background-image: url(https://a.imagem.app/batHpt.png);
            background-size: cover;
            font-size: 16px;
             }}


            </style>
            """
    st.markdown(page_bg_imge, unsafe_allow_html=True)
    r_quadrada.raiz()


elif paginaselecionada == 'Conversão de temperatura':
    page_bg_imge = f"""
                    <style>
                [data-testid ="stAppViewContainer"] {{
                background-image: url(https://a.imagem.app/batHpt.png);
                background-size: cover;
                font-size: 16px;
                 }}


                </style>
                """
    st.markdown(page_bg_imge, unsafe_allow_html=True)


    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32


    def celsius_to_kelvin(celsius):
        return celsius + 273.15


    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit + 459.67) * 5 / 9


    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15


    def kelvin_to_fahrenheit(kelvin):
        return kelvin * 9 / 5 - 459.67


    def main():
        st.title("Conversor de Temperatura")

        temperature = st.number_input("Digite a temperatura:")

        unit_from = st.selectbox("Converter de:", ["Celsius", "Fahrenheit", "Kelvin"])
        unit_to = st.selectbox("Converter para:", ["Celsius", "Fahrenheit", "Kelvin"])

        if st.button("Converter"):
            converted_temperature = None

            if unit_from == "Celsius":
                if unit_to == "Fahrenheit":
                    converted_temperature = celsius_to_fahrenheit(temperature)
                elif unit_to == "Kelvin":
                    converted_temperature = celsius_to_kelvin(temperature)
                else:
                    converted_temperature = temperature
            elif unit_from == "Fahrenheit":
                if unit_to == "Celsius":
                    converted_temperature = fahrenheit_to_celsius(temperature)
                elif unit_to == "Kelvin":
                    converted_temperature = fahrenheit_to_kelvin(temperature)
                else:
                    converted_temperature = temperature
            else:
                if unit_to == "Celsius":
                    converted_temperature = kelvin_to_celsius(temperature)
                elif unit_to == "Fahrenheit":
                    converted_temperature = kelvin_to_fahrenheit(temperature)
                else:
                    converted_temperature = temperature

            st.write(f"{temperature} {unit_from} é igual a {converted_temperature:.2f} {unit_to}")
    if __name__ == '__main__':
        main()

elif paginaselecionada == 'Conversão de bases':
    page_bg_imge = f"""
                <style>
            [data-testid ="stAppViewContainer"] {{
            background-image: url(https://a.imagem.app/batHpt.png);
            background-size: cover;
            font-size: 16px;
             }}
            [data-baseweb="notificacion"] {{
             background-color: rgba(0,0,0,0)
             
             }}

            </style>
            """
    st.markdown(page_bg_imge, unsafe_allow_html=True)

    bases_num.bases()

elif paginaselecionada == 'Conversão de Moedas':
    page_bg_imge = f"""
                <style>
            [data-testid ="stAppViewContainer"] {{
            background-image: url(https://a.imagem.app/batHpt.png);
            background-size: cover;
            font-size: 16px;
            
             }}
            

            </style>
            """
    st.markdown(page_bg_imge, unsafe_allow_html=True)
    c_moed.moedas()
