TURBO RACE LIVE — Entrada automática por novos seguidores

1. Abra index.html no navegador do MacBook.
2. O jogo tenta conectar em ws://127.0.0.1:8765 (relay local).
3. O relay deve receber eventos de uma integração TikTok LIVE compatível,
   validar que são eventos reais e confirmados de NOVOS seguidores, e emitir:
   {"type":"follow","username":"nome","eventId":"id-unico","confirmed":true}
4. O jogo adiciona o seguidor imediatamente se houver vaga (até 8 carros),
   ou coloca em fila para a próxima rodada.
5. Comentários não são necessários. Eventos repetidos com o mesmo eventId
   são ignorados durante a sessão.
6. Sem relay, use TESTAR FOLLOW para demonstrar a mecânica.

IMPORTANTE: Este pacote NÃO acessa diretamente a API do TikTok nem comprova
que um usuário seguiu a conta. É necessário um conector externo autorizado e
compatível, capaz de receber eventos de follow e validar sua autenticidade.
Não confie em eventos de fontes públicas não autenticadas. Não exponha o
relay na internet sem autenticação. O relay de exemplo abaixo é apenas local.

Para simular um relay local: instale Python 3 e a biblioteca websockets
(python3 -m pip install websockets), depois execute:
python3 relay_teste.py

Não deixe a transmissão sem supervisão e observe as regras de LIVE do TikTok.
