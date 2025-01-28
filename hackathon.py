import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Função para calcular a poupança
def calcular_poupanca(poupanca_atual, rendimento=0.005):
    return poupanca_atual * (1 + rendimento)

# Função para salvar os dados em um arquivo CSV
def salvar_dados(df, ano, mes):
    if not os.path.exists('dados_financeiros'):
        os.makedirs('dados_financeiros')
    filename = f"dados_financeiros/dados_financeiros_{ano}_{mes}.csv"
    df.to_csv(filename, index=False)
    return filename

# Função para carregar os dados de um arquivo CSV
def carregar_dados(ano, mes):
    filename = f"dados_financeiros/dados_financeiros_{ano}_{mes}.csv"
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        st.error(f"Arquivo {filename} não encontrado.")
        return pd.DataFrame()

# Streamlit App
st.title("Gerenciador Financeiro com Gráficos e Comparativos")

# Entrada de dados
st.header("Insira seus dados financeiros")
ano = st.number_input("Ano:", min_value=2000, step=1, value=2025)
mes = st.selectbox("Mês:", ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
salario = st.number_input("Salário:", min_value=0.0, step=0.01)
extra = st.number_input("Renda extra:", min_value=0.0, step=0.01)
aluguel = st.number_input("Aluguel:", min_value=0.0, step=0.01)
agua = st.number_input("Água:", min_value=0.0, step=0.01)
luz = st.number_input("Luz:", min_value=0.0, step=0.01)
internet = st.number_input("Internet:", min_value=0.0, step=0.01)
comida = st.number_input("Comida:", min_value=0.0, step=0.01)
combustivel = st.number_input("Combustível:", min_value=0.0, step=0.01)
lanche = st.number_input("Lanche:", min_value=0.0, step=0.01)
passeio = st.number_input("Passeio:", min_value=0.0, step=0.01)
viagem = st.number_input("Viagem:", min_value=0.0, step=0.01)

# Cálculos
renda_total = salario + extra
gastos_essenciais = aluguel + agua + luz + internet + comida + combustivel
gastos_supérfluos = lanche + passeio + viagem
poupanca = 0.0
valor_extra = 0.0

# Recuperar valor da poupança do mês anterior, se houver
if "poupanca_anterior" not in st.session_state:
    st.session_state.poupanca_anterior = 0.0
if "valor_extra_anterior" not in st.session_state:
    st.session_state.valor_extra_anterior = 0.0

poupanca += st.session_state.poupanca_anterior

gastos_totais = gastos_essenciais + gastos_supérfluos
limite_gastos = renda_total * 0.7
poupanca_mensal = renda_total * 0.1

# Adicionar a poupança mensal
poupanca += poupanca_mensal

if gastos_totais > limite_gastos:
    excesso = gastos_totais - limite_gastos
    st.write("\n**ALERTA**: Você ultrapassou o limite de 70% dos seus gastos.")
    st.write(f"Será necessário ajustar seus gastos em R${excesso:.2f} para equilibrar as finanças.")
    if poupanca >= excesso:
        poupanca -= excesso
        valor_extra = excesso * 1.005  # Valor a ser reposto, ajustado pelo rendimento
        st.write(f"R${excesso:.2f} foi retirado da poupança.")
        st.write(f"Para o próximo mês, será necessário devolver R${valor_extra:.2f} à poupança.")
    else:
        st.write(f"Você precisa cortar R${excesso - poupanca:.2f} dos gastos. Sua poupança é insuficiente.")
else:
    st.write("\nParabéns! Seus gastos estão dentro do limite de 70%.")
    st.write(f"Sua poupança foi atualizada para R${poupanca:.2f}.")

# Atualizar valor extra na poupança
st.session_state.valor_extra_anterior = valor_extra
st.session_state.poupanca_anterior = calcular_poupanca(poupanca)

# Criação do DataFrame
data = {
    "Categoria": ["Essenciais", "Supérfluos", "Poupança"],
    "Valor": [gastos_essenciais, gastos_supérfluos, poupanca],
    "Tipo": ["Gasto", "Gasto", "Poupança"],
    "Mês": [mes, mes, mes],
    "Ano": [ano, ano, ano],
}
df = pd.DataFrame   