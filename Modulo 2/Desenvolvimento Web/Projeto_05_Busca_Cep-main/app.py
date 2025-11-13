import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####

st.title("Busca cep")
##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####
st.sidebar.title("buscar por cep")
st.sidebar.image("logo.png")
st.sidebar.write("Aplicação para buscar endereço a partir do CEP e mostrar localização no mapa")
opcao = st.sidebar.selectbox("Escolha a opção desejada:", opcoes)

##### BOTÃO BUSCAR CEP #####

if opcao == "Buscar CEP":
    st.image("principal.png")
    st.subheader("Buscar o endereço pelo CEP")
    cep = st.text_input("Digite o CEP (somente o número)")

    if st.button("Buscar"):
            if len(cep) != 8 or not cep.isdigit():
                st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
            else:
                try:
                    endereco = BuscarCep.buscar_cep(cep)
                    if endereco:
                        st.success("Endereço encontrado:")
                        st.write(f"CEP: {endereco[0]}")
                        st.write(f"Enderço: {endereco[1]}")
                        st.write(f"Bairro: {endereco[2]}")
                        st.write(f"Cidade: {endereco[3]}")
                        st.write(f"Estado: {endereco[4]}")


                        ##mapas
                        st.title("Localização no Mapa")
                        df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                        st.map(df, zoom=15)
                    else:
                        st.error("CEP não encontrado")
                except Exception as e:
                            st.error(f"Ocorreu um erro ao buscar o CEP: {e}")


##### BOTÃO DESCOBRIR CEP #####
elif opcao == "Descobrir CEP":
      st.header("descobrir CEP pelo endereço")
      endereço_usuario = st.text_input("Digite o endereço (ex: Rua Olga Barueri, SP):")

      if st.button("Descobrir"):
            if not endereço_usuario.strip():
                  st.error("por favor, insira um endereço válido")
            else:
                try:
                  resultado = BuscarCep.descobrir_cep(endereço_usuario) 
                  st.success("Link de byusca no Google:")
                  st.write(resultado)
                except Exception as e:
                     st.error(f"Ocorreu um erro ao descobrir o CEP: {e}")
