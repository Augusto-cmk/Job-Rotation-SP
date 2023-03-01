import pandas as pd

df = pd.read_json("dados.json")
df = df[df['valor'] != 0] # Ignorando os valores zerados

menorFaturamento = df['valor'].min() # Obetendo o menor valor
maiorFaturamento = df['valor'].max() # Obtendo o meior valor
media = df['valor'].mean() # Obtendo a média dos valores
qtdSuperior = len(df[df['valor'] > media]) # Obtendo a quanditdade dos valores cujo valor é superior a média

print(f"Menor Faturamento {menorFaturamento}\nMaior Faturamento {maiorFaturamento}\nQuantidade de dias cujo valor é superior a média mensal {qtdSuperior}")
