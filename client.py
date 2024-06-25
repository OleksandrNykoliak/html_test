import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)



async def chat_client():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                message = input("Введіть ваше повідомлення: ")
                logging.info(f"Відправлене повідомлення: {message}") 
                await websocket.send(message)
                response = await websocket.recv()
                logging.info(f"Отримане повідомлення: {response}")
                
                print(f"Отримане повідомлення: {response}")
            except websockets.exceptions.ConnectionClosedError:
                print("Підключення було втрачено. Спробуйте пізніше.")
                break

asyncio.get_event_loop().run_until_complete(chat_client())


