"""Relay LOCAL DE TESTE. Não conecta ao TikTok e não confirma seguidores reais."""
import asyncio, json
import websockets
clients = set()
async def handler(ws):
    clients.add(ws)
    try:
        async for _ in ws:
            pass
    finally:
        clients.discard(ws)
async def main():
    async with websockets.serve(handler, '127.0.0.1', 8765):
        print('Relay local de TESTE em ws://127.0.0.1:8765')
        i=0
        while True:
            name=(await asyncio.to_thread(input,'Nome do seguidor de TESTE (Enter para pular): ')).strip()
            if not name: continue
            i+=1
            msg=json.dumps({'type':'follow','username':name,'eventId':f'teste-{i}','confirmed':True})
            for ws in list(clients):
                await ws.send(msg)
asyncio.run(main())
