import asyncio

"""
async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Recebido {message} de {addr}")

    print("Envie: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Fechando a conexão")
    writer.close()
"""

# Lista para armazenar os dados dos sensores
dados_do_sensor_1 = []
dados_do_sensor_2 = []
dados_do_sensor_3 = []


async def gerenciar_sensor_1(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Conexão de sensor estabelecida com {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break

        mensagem = data.decode()
        print(f"Dados recebidos do sensor 1 {addr}: {mensagem}")

        # Armazena os dados do sensor na lista
        dados_do_sensor_1.append((addr, mensagem))

        # Responde ao sensor (opcional)
        response = "Dados do Sensor 1 recebidos com sucesso!"
        writer.write(response.encode())
        await writer.drain()

    print(f"Fechando a conexão com Sensor 1 {addr}")
    writer.close()
    
# Função para gerenciar o sensor 2
async def gerenciar_sensor_2(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"CONEXÃO DE SESNOR 2 ESTABELECIDA COM {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break

        mensagem = data.decode()
        print(f"Dados recebidos do Sensor 2 {addr}: {mensagem}")

        # Armazena os dados do Sensor 2 na lista
        dados_do_sensor_2.append((addr, mensagem))

        # Responde ao Sensor 2 (opcional)
        response = "Dados do Sensor 2 recebidos com sucesso!"
        writer.write(response.encode())
        await writer.drain()

    print(f"Fechando a conexão com Sensor 2 {addr}")
    writer.close()

# Função para gerenciar o sensor 3
async def gerenciar_sensor_3(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Conexão de Sensor 3 estabelecida com {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break

        mensagem = data.decode()
        print(f"Dados recebidos do Sensor 3 {addr}: {mensagem}")

        # Armazena os dados do Sensor 3 na lista
        dados_do_sensor_3.append((addr, mensagem))

        # Responde ao Sensor 3 (opcional)
        response = "Dados do Sensor 3 recebidos com sucesso!"
        writer.write(response.encode())
        await writer.drain()

    print(f"Fechando a conexão com Sensor 3 {addr}")
    writer.close()

async def main():
    #server = await asyncio.start_server(gerenciar_sensor, '127.0.0.1', 8888)
    server_1 = await asyncio.start_server(gerenciar_sensor_1, '127.0.0.1', 8888)
    server_2 = await asyncio.start_server(gerenciar_sensor_2, '127.0.0.1', 8889)
    server_3 = await asyncio.start_server(gerenciar_sensor_3, '127.0.0.1', 8890)

    async with server_1, server_2, server_3:
        print("Seridor de Ananlise de Sensores Trabalhando...")
        #await server.serve_forever()
        await asyncio.gather(
            server_1.serve_forever(),
            server_2.serve_forever(),
            server_3.serve_forever()
        )

asyncio.run(main())