import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

message_broker = []

connected = set()

async def chat_server(websocket, path):
    connected.add(websocket)
    logging.info(f"Підключено {websocket}")
    try:
        async for message in websocket:
            message_broker.append(message)
            print(f"Отримане повідомлення: {message_broker}")
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        # Видаляємо підключення, коли клієнт відключається
        connected.remove(websocket)

start_server = websockets.serve(chat_server, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

