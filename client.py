import asyncio
import random
import time

"""
async def send_message(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    
    print(f'Enviando: {message}')
    writer.write(message.encode())
    
    data = await reader.read(100)
    print(f'Recebido: {data.decode()}')

    writer.close()
    await writer.wait_closed()
"""

dados_exemplos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

"""
async def enviar_dados(reader, writer):
    sensor_id = writer.get_extra_info('peername')
    print(f"Conexão de sensor estabelecida com {sensor_id}")

    while True:
        # Simula a leitura de dados do sensor (gera um valor aleatório)
        dados_sensor = random.choice(dados_exemplos)
        mensagem = f"Dado do sensor {sensor_id}: {dados_sensor}"

        # Envia os dados para o servidor
        writer.write(mensagem.encode())
        await writer.drain()

        print(f"Dados enviados para o servidor: {mensagem}")

        # Aguarda um intervalo de tempo antes de enviar o próximo dado
        await asyncio.sleep(random.uniform(1, 5))
"""


async def enviar_dados(sensor_id, server_port):
    reader, writer = await asyncio.open_connection('127.0.0.1', server_port)

    print(f"Conexão com Sensor {sensor_id} estabelecida")

    while True:
        # Simula a leitura de dados do sensor (gera um valor aleatório)
        dados_sensor = random.uniform(0.0, 100.0)
        mensagem = f"Dado do sensor {sensor_id}: {dados_sensor}"

        # Envia os dados para o servidor do sensor correspondente
        writer.write(mensagem.encode())
        await writer.drain()

        print(f"Dados enviados para Sensor {sensor_id}: {mensagem}")

        # Aguarda um intervalo de tempo antes de enviar o próximo dado
        await asyncio.sleep(random.uniform(1, 5))
        
async def main():
    # Define os IDs e portas dos sensores
    sensores = [
        {"id": "Sensor-1", "port": 8888},
        {"id": "Sensor-2", "port": 8889},
        {"id": "Sensor-3", "port": 8890},
    ]

    # Inicia tarefas para conectar e enviar dados para cada sensor
    for sensor in sensores:
        asyncio.create_task(enviar_dados(sensor["id"], sensor["port"]))

    while True:
        await asyncio.sleep(1)

asyncio.run(main())

"""
async def main():
    
    num_sensores = 3  # Define o número de sensores (clientes) que deseja iniciar

    for i in range(num_sensores):
        sensor_id = f"Sensor-{i + 1}"
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

        # Define o sensor_id como o nome do cliente (sensor)
        writer.write(sensor_id.encode())
        await writer.drain()

        asyncio.create_task(enviar_dados(reader, writer))
    
    while True:
      await asyncio.sleep(1)  
      #await send_message("Olá de novo, Servidor!")

asyncio.run(main())
"""