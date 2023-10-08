import asyncio

async def send_message(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    
    print(f'Enviando: {message}')
    writer.write(message.encode())
    
    data = await reader.read(100)
    print(f'Recebido: {data.decode()}')

    writer.close()
    await writer.wait_closed()

async def main():
    while True:
      await asyncio.sleep(1)  
      await send_message("Olá de novo, Servidor!")

asyncio.run(main())