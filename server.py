import websockets
import asyncio

async def handler(ws):
    async for code in ws:
        try:
            exec_locals = {}
            exec(code, {}, exec_locals)
            await ws.send(str(exec_locals))
        except Exception as e:
            await ws.send("Erreur: " + str(e))

asyncio.run(websockets.serve(handler, "0.0.0.0", 8765))
