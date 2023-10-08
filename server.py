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

async def gerenciar_sensor(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Conexão de sensor estabelecida com {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            break

        mensagem = data.decode()
        print(f"Dados recebidos do sensor {addr}: {mensagem}")

        # Armazena os dados do sensor na lista
        dados_do_sensor_1.append((addr, mensagem))

        # Responde ao sensor (opcional)
        response = "Dados recebidos com sucesso!"
        writer.write(response.encode())
        await writer.drain()

    print(f"Fechando a conexão com {addr}")
    writer.close()


async def main():
    server = await asyncio.start_server(gerenciar_sensor, '127.0.0.1', 8888)
    async with server:
        print("Seridor de Ananlise de Sensores Trabalhando...")
        await server.serve_forever()

asyncio.run(main())