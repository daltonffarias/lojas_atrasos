import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados do GitHub
def load_data():
    url = "https://github.com/daltonffarias/lojas_atrasos/blob/main/inadimplencia_lojas.csv"
    data = pd.read_csv(url)
    return data

# Função para calcular a taxa de inadimplência
def calculate_default_rate(data):
    total_sales = data['Valor Compra (R$)'].sum()
    default_sales = data[data['Status Pagamento'].isin(['Atraso', 'Inadimplente'])]['Valor Compra (R$)'].sum()
    default_rate = (default_sales / total_sales) * 100
    return default_rate

# Função para plotar a distribuição de atraso
def plot_delay_distribution(data):
    delay_bins = [0, 30, 60, 90, 180, np.inf]
    delay_labels = ['0-30', '31-60', '61-90', '91-180', '180+']
    data['Dias em Atraso'] = pd.cut(data['Dias em Atraso'], bins=delay_bins, labels=delay_labels)
    delay_distribution = data[data['Status Pagamento'] == 'Atraso'].groupby('Dias em Atraso').size()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=delay_distribution.index, y=delay_distribution.values)
    plt.title('Distribuição de Atraso por Faixa de Dias')
    plt.xlabel('Faixa de Dias em Atraso')
    plt.ylabel('Quantidade de Compras')
    st.pyplot()

# Função para analisar o perfil de clientes inadimplentes
def analyze_default_profile(data):
    default_customers = data[data['Status Pagamento'] == 'Inadimplente']
    avg_purchase_value = default_customers['Valor Compra (R$)'].mean()
    purchase_frequency = default_customers['ID Cliente'].value_counts().mean()
    
    st.write(f"Valor Médio das Compras: R${avg_purchase_value:.2f}")
    st.write(f"Frequência Média de Compras: {purchase_frequency:.2f}")

# Função principal
def main():
    st.title("Análise de Inadimplência")
    
    # Botão para carregar os dados
    if st.button("Carregar Dados do GitHub"):
        data = load_data()
        st.write("Dados carregados com sucesso!")
        
        # Análise da Situação Atual da Inadimplência
        st.header("Análise da Situação Atual da Inadimplência")
        default_rate = calculate_default_rate(data)
        st.write(f"Taxa de Inadimplência: {default_rate:.2f}%")
        
        # Distribuição de Atraso
        st.header("Distribuição de Atraso")
        plot_delay_distribution(data)
        
        # Perfil de Clientes Inadimplentes
        st.header("Perfil de Clientes Inadimplentes")
        analyze_default_profile(data)
        
        # Estimativa da Inadimplência Futura
        st.header("Estimativa da Inadimplência Futura")
        st.write("Aqui você pode adicionar a lógica para estimar a inadimplência futura.")
        
        # Comparação com Outras Lojas
        st.header("Comparação com Outras Lojas")
        st.write("Aqui você pode adicionar a lógica para comparar a inadimplência com outras lojas.")
        
        # Conclusão
        st.header("Conclusão")
        st.write("Aqui você pode adicionar a conclusão sobre o estado atual da loja.")

if __name__ == "__main__":
    main()
