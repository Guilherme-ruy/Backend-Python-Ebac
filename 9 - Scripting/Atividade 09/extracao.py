import os
import time
import json
from random import random
from datetime import datetime

import requests

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

# Definindo o caminho de forma mais robusta
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'taxa-cdi.csv')

# Captando a taxa CDI do site do BCB

try:
  response = requests.get(url=URL)
  response.raise_for_status()
except requests.HTTPError as exc:
  print("Dado não encontrado, continuando.")
  cdi = None
except Exception as exc:
  print("Erro, parando a execução.")
  raise exc
else:
  dado = json.loads(response.text)[-1]['valor']

# Criando a variável data e hora

for _ in range(0, 10):

  data_e_hora = datetime.now()
  data = datetime.strftime(data_e_hora, '%Y/%m/%d')
  hora = datetime.strftime(data_e_hora, '%H:%M:%S')

  cdi = float(dado) + (random() - 0.5)

  # Verificando se o arquivo "taxa-cdi.csv" existe

  if not os.path.exists(csv_file_path):

    with open(file=csv_file_path, mode='w', encoding='utf8') as fp:
      fp.write('data,hora,taxa\n')

  # Salvando dados no arquivo "taxa-cdi.csv"

  with open(file=csv_file_path, mode='a', encoding='utf8') as fp:
    fp.write(f'{data},{hora},{cdi}\n')

  time.sleep(1)
  
print("Sucesso")