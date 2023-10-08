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

async def enviar_dados(reader, writer):
    sensor_id = writer.get_extra_info('peername')
    print(f"Conexão de sensor estabelecida com {sensor_id}")

    while True:
        # Simula a leitura de dados do sensor (gera um valor aleatório)
        dados_sensor = random.uniform(0.0, 100.0)
        mensagem = f"Dado do sensor {sensor_id}: {dados_sensor}"

        # Envia os dados para o servidor
        writer.write(mensagem.encode())
        await writer.drain()

        print(f"Dados enviados para o servidor: {mensagem}")

        # Aguarda um intervalo de tempo antes de enviar o próximo dado
        await asyncio.sleep(random.uniform(1, 5))


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