import os
import time
import json
import sys
from random import random
from datetime import datetime

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Função para extrair dados e salvar no CSV
def extrair_dados_csv():
    URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

    try:
        response = requests.get(url=URL)
        response.raise_for_status()
    except requests.HTTPError:
        print("Dado não encontrado, continuando.")
        return None
    except Exception as exc:
        print("Erro ao buscar os dados, parando a execução.")
        raise exc

    dado = json.loads(response.text)[-1]['valor']
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, 'taxa-cdi.csv')

    # Gerando dados com variação e salvando no CSV
    for _ in range(0, 10):
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, '%Y/%m/%d')
        hora = datetime.strftime(data_e_hora, '%H:%M:%S')

        cdi = float(dado) + (random() - 0.5)

        if not os.path.exists(csv_file_path):
            with open(file=csv_file_path, mode='w', encoding='utf8') as fp:
                fp.write('data,hora,taxa\n')

        with open(file=csv_file_path, mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi}\n')

        time.sleep(1)

    print("Dados extraídos e salvos no arquivo taxa-cdi.csv.")
    return csv_file_path


# Função para gerar o gráfico
def gerar_grafico(csv_file_path, nome_grafico):
    df = pd.read_csv(csv_file_path)

    # Criando o gráfico
    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)

    # Salvando o gráfico no mesmo diretório
    current_dir = os.path.dirname(os.path.abspath(__file__))
    grafico_path = os.path.join(current_dir, f'{nome_grafico}.png')
    grafico.get_figure().savefig(grafico_path)

    # Imprimindo o caminho que o grafico foi salvo
    print(f"Gráfico salvo em: {grafico_path}")

# Função principal
def main():
    if len(sys.argv) < 2:
        print("Uso correto: python analise.py <nome-do-grafico>")
        sys.exit(1)

    nome_grafico = sys.argv[1]

    # Extraindo dados e gerando CSV
    csv_file_path = extrair_dados_csv()

    # Gerando o gráfico
    if csv_file_path:
        gerar_grafico(csv_file_path, nome_grafico)


if __name__ == '__main__':
    main()