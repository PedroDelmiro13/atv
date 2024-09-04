import pandas as pd

dados_empresa = { #criei o df com os dados que pedia na questão
    'estado': ['SP', 'RJ', 'MG', 'ES', 'Outros'],
    'faturamento': [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
}

df = pd.DataFrame(dados_empresa)
total_mensal = df['faturamento'].sum() #somei todas as faturas
df['Percentual'] = round((df['faturamento'] / total_mensal) * 100, 2).apply(lambda x: f'{x:.2f}%') #calculei o percentual usando faturamento dividido pelo total, e formatei para aparecer com 2 casas decimais
print(df)

