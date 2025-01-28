import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit App
st.title("Gerenciador Financeiro com Gráficos e Comparativos")

# Entrada de dados
st.header("Insira seus dados financeiros")
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

gastos_totais = gastos_essenciais + gastos_supérfluos
limite_gastos = renda_total * 0.7
poupanca_mensal = renda_total * 0.1
poupanca += poupanca_mensal

if gastos_totais > limite_gastos:
    excesso = gastos_totais - limite_gastos
    st.write("\n**ALERTA**: Você ultrapassou o limite de 70% dos seus gastos.")
    st.write(f"Será necessário ajustar seus gastos em R${excesso:.2f} para equilibrar as finanças.")
    if poupanca >= excesso:
        poupanca -= excesso
        st.write(f"R${excesso:.2f} foi retirado da poupança.")
    else:
        st.write(f"Você precisa cortar R${excesso - poupanca:.2f} dos gastos. Sua poupança é insuficiente.")
else:
    st.write("\nParabéns! Seus gastos estão dentro do limite de 70%.")
    st.write(f"Sua poupança foi atualizada para R${poupanca:.2f}.")

# Criação do DataFrame
data = {
    "Categoria": ["Essenciais", "Supérfluos", "Poupança"],
    "Valor": [gastos_essenciais, gastos_supérfluos, poupanca],
    "Tipo": ["Gasto", "Gasto", "Poupança"],
    "Mês": ["Atual", "Atual", "Atual"],
}
df = pd.DataFrame(data)

# Gráfico de Barras
st.subheader("Gráfico de Barras - Comparativo de Gastos")
fig_bar = px.bar(df, x="Categoria", y="Valor", color="Tipo", barmode="group", title="Gastos Essenciais vs Supérfluos")
st.plotly_chart(fig_bar)

# Gráfico de Pizza
st.subheader("Gráfico de Pizza - Distribuição dos Gastos")
fig_pizza = px.pie(df, names="Categoria", values="Valor", title="Distribuição dos Gastos")
st.plotly_chart(fig_pizza)

# Gráfico de Linha
st.subheader("Gráfico de Linha - Tendência Mensal")
df_linha = pd.DataFrame({
    "Mês": ["Janeiro", "Fevereiro", "Março"],
    "Essenciais": [gastos_essenciais, gastos_essenciais * 1.05, gastos_essenciais * 0.9],
    "Supérfluos": [gastos_supérfluos, gastos_supérfluos * 0.8, gastos_supérfluos * 1.1],
    "Poupança": [poupanca, poupanca * 1.02, poupanca * 1.03],
}).melt(id_vars="Mês", var_name="Categoria", value_name="Valor")

fig_linha = px.line(df_linha, x="Mês", y="Valor", color="Categoria", markers=True, title="Tendência Mensal dos Gastos")
st.plotly_chart(fig_linha)

# Exportar Dados
st.subheader("Exportar Dados")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(label="Baixar Dados (CSV)", data=csv, file_name="dados_financeiros.csv", mime="text/csv")