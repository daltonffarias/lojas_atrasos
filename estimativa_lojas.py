import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Simulação de dados
data = {
    'Data': pd.date_range(start='2024-01-01', periods=12, freq='M'),
    'Inadimplência': np.random.uniform(5, 15, 12)
}
df = pd.DataFrame(data)

# Layout do Streamlit
st.title('Análise de Inadimplência')

# Exibir dados históricos
st.subheader('Histórico de Inadimplência')
st.line_chart(df.set_index('Data'))

# Estimativa da Inadimplência Futura
st.subheader('Estimativa da Inadimplência Futura')

# Criando um modelo de regressão linear
X = np.array(range(len(df))).reshape(-1, 1)
y = df['Inadimplência'].values
modelo = LinearRegression()
modelo.fit(X, y)

# Previsão para os próximos 6 meses
future_dates = [df['Data'].iloc[-1] + timedelta(days=30 * i) for i in range(1, 7)]
X_future = np.array(range(len(df), len(df) + 6)).reshape(-1, 1)
future_predictions = modelo.predict(X_future)

future_df = pd.DataFrame({'Data': future_dates, 'Inadimplência Estimada': future_predictions})

# Melhor visualização com Matplotlib
fig, ax = plt.subplots()
ax.plot(df['Data'], df['Inadimplência'], marker='o', label='Histórico', linestyle='-')
ax.plot(future_df['Data'], future_df['Inadimplência Estimada'], marker='o', linestyle='--', color='red', label='Previsão')
ax.set_xlabel('Data')
ax.set_ylabel('Inadimplência')
ax.set_title('Previsão de Inadimplência')
ax.legend()
st.pyplot(fig)

# Comparação com Outras Lojas
st.subheader('Comparação com Outras Lojas')
lojas = ['Loja A', 'Loja B', 'Loja C', 'Sua Loja']
inadimplencia_lojas = [10, 12, 8, df['Inadimplência'].mean()]

comparacao_df = pd.DataFrame({'Loja': lojas, 'Inadimplência Média': inadimplencia_lojas})

fig, ax = plt.subplots()
ax.bar(comparacao_df['Loja'], comparacao_df['Inadimplência Média'], color=['blue', 'blue', 'blue', 'red'])
ax.set_ylabel('Inadimplência Média')
ax.set_title('Comparação entre Lojas')
for i, v in enumerate(inadimplencia_lojas):
    ax.text(i, v + 0.3, f'{v:.1f}%', ha='center', fontsize=10)
st.pyplot(fig)

# Conclusão
st.subheader('Conclusão')
st.write('Com base na análise, observamos que a inadimplência da loja está dentro da média do mercado. Recomenda-se monitorar de perto as tendências futuras para evitar aumentos inesperados.')
