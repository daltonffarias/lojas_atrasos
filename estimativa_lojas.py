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
st.line_chart(pd.concat([df.set_index('Data'), future_df.set_index('Data')]))

# Comparação com Outras Lojas
st.subheader('Comparação com Outras Lojas')
lojas = ['Loja A', 'Loja B', 'Loja C', 'Sua Loja']
inadimplencia_lojas = [10, 12, 8, df['Inadimplência'].mean()]

comparacao_df = pd.DataFrame({'Loja': lojas, 'Inadimplência Média': inadimplencia_lojas})
st.bar_chart(comparacao_df.set_index('Loja'))

# Conclusão
st.subheader('Conclusão')
st.write('Com base na análise, observamos que a inadimplência da loja está dentro da média do mercado. Recomenda-se monitorar de perto as tendências futuras para evitar aumentos inesperados.')
