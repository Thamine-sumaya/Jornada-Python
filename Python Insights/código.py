import pandas as pd
tabela = pd.read_csv('Cópia de cancelamentos_sample.csv') 
tabela = tabela.drop(columns=["CustomerID", "idade"])
print(tabela) 
print(tabela.info())
tabela = tabela.dropna()
print(tabela['cancelou'].value_counts(normalize=True))
import plotly.express as px
for coluna in tabela.columns:
	grafico = px.histogram(tabela, x=coluna, color="cancelou")
#mostrar gráfico
grafico.show()
#porcentagem de assinantes que cancelaram, sem contabilizar os assinantes por mês, mais de 4 ligações do call center e mais de 20 dias de atraso
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts(normalize=True))
