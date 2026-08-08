import aiohttp
import asyncio
import json

async def notification_client():
    async with aiohttp.ClientSession() as session:
        # Łączę się z odpowiednim endpointem WebSocket
        async with session.ws_connect('ws://localhost:8080/ws/notifications') as ws:
            print("--- Czekam na ważne powiadomienia systemowe ---")
            
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    # Zamieniam otrzymany tekst JSON z powrotem na słownik Pythona
                    data = json.loads(msg.data)
                    print(f"\n[🔔 DZWONEK] NOWE POWIADOMIENIE: {data.get('notification')}")

if __name__ == '__main__':
    asyncio.run(notification_client())