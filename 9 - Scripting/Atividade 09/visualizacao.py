import os
import pandas as pd
import seaborn as sns

# Definindo o caminho de forma robusta para o arquivo CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'taxa-cdi.csv')

# Extraindo as colunas hora e taxa do arquivo CSV
df = pd.read_csv(csv_file_path)

# Criando o gráfico
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)

# Salvando o gráfico no mesmo diretório
grafico_path = os.path.join(current_dir, 'grafico.png')
grafico.get_figure().savefig(grafico_path)

print(f"Gráfico salvo em: {grafico_path}")