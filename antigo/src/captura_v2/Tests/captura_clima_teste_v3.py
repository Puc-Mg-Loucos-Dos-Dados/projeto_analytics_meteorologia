import requests
import mysql.connector
from datetime import datetime, timedelta

# Dados de acesso ao banco de dados
user = 'root'
password = '123456'
host = 'localhost'
database = 'dw_salao_de_beleza'  # Substitua pelo nome do seu banco de dados

# Chave de API OpenWeather
API_KEY = "221f164d35f7154a527c7b3146fa2129"

# Coordenadas de Salvador
latitude = -12.9704
longitude = -38.5124

# Definindo a data inicial e a data final
data_inicial = datetime(2023, 5, 2)
data_final = datetime.now()

# Função para converter de Kelvin para Celsius
def kelvin_para_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Função para obter dados climáticos da API OpenWeather
def obter_temperatura(data):
    print("Iniciando coleta")
    link = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={latitude}&lon={longitude}&date={data.strftime('%Y-%m-%d')}&appid={API_KEY}"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    temperatura_min = kelvin_para_celsius(requisicao_dic['temperature']['min'])
    temperatura_max = kelvin_para_celsius(requisicao_dic['temperature']['max'])
    temperatura_tarde = kelvin_para_celsius(requisicao_dic['temperature']['afternoon'])
    temperatura_noite = kelvin_para_celsius(requisicao_dic['temperature']['night'])
    temperatura_noite = kelvin_para_celsius(requisicao_dic['temperature']['evening'])
    temperatura_manha = kelvin_para_celsius(requisicao_dic['temperature']['morning'])
    return temperatura_min, temperatura_max, temperatura_tarde, temperatura_noite, temperatura_manha

# Loop para coletar os dados para cada data
while data_inicial <= data_final:
    temperatura_min, temperatura_max, temperatura_tarde, temperatura_noite, temperatura_manha = obter_temperatura(data_inicial)
    if temperatura_min is not None and temperatura_max is not None and temperatura_tarde is not None and temperatura_noite is not None and temperatura_manha is not None:
        # Conectar ao banco de dados
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = db_connection.cursor()

        # Inserir os dados no banco de dados
        insert_query = "INSERT INTO d_clima (temperatura_min, temperatura_max, temperatura_tarde, temperatura_noite, temperatura_manha, dia, data_atual) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data_insercao = (temperatura_min, temperatura_max, temperatura_tarde, temperatura_noite, temperatura_manha, data_inicial.strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
        cursor.execute(insert_query, data_insercao)
        db_connection.commit()

        # Fechar a conexão com o banco de dados
        cursor.close()
        db_connection.close()

    # Incrementar a data inicial em um dia
    data_inicial += timedelta(days=1)

print("Dados coletados e inseridos no banco de dados com sucesso.")
