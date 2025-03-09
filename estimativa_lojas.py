import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
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
fig_hist = px.line(df, x='Data', y='Inadimplência', markers=True, title='Histórico de Inadimplência')
st.plotly_chart(fig_hist)

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

# Gráfico interativo com Plotly
fig_forecast = go.Figure()
fig_forecast.add_trace(go.Scatter(x=df['Data'], y=df['Inadimplência'], mode='lines+markers', name='Histórico'))
fig_forecast.add_trace(go.Scatter(x=future_df['Data'], y=future_df['Inadimplência Estimada'], mode='lines+markers', name='Previsão', line=dict(dash='dash', color='red')))
fig_forecast.update_layout(title='Previsão de Inadimplência', xaxis_title='Data', yaxis_title='Inadimplência')
st.plotly_chart(fig_forecast)

# Comparacao com Outras Lojas
st.subheader('Comparacão com Outras Lojas')
lojas = ['Loja A', 'Loja B', 'Loja C', 'Sua Loja']
inadimplencia_lojas = [10, 12, 8, df['Inadimplência'].mean()]
comparacao_df = pd.DataFrame({'Loja': lojas, 'Inadimplência Média': inadimplencia_lojas})

fig_comparacao = px.bar(comparacao_df, x='Loja', y='Inadimplência Média', color='Loja', title='Comparacão entre Lojas')
st.plotly_chart(fig_comparacao)

# Conclusão
st.subheader('Conclusão')
st.write('Com base na análise, observamos que a inadimplência da loja está dentro da média do mercado. Recomenda-se monitorar de perto as tendências futuras para evitar aumentos inesperados.')
