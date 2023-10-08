import asyncio

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

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())