import asyncio
import websockets

async def handler(ws):
    async for code in ws:
        try:
            exec_locals = {}
            exec(code, {}, exec_locals)
            await ws.send(str(exec_locals))
        except Exception as e:
            await ws.send("Erreur: " + str(e))

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Serveur Python prêt sur le port 8765")
        await asyncio.Future()  # boucle infinie propre

asyncio.run(main())
