import requests
import json

with open("token.txt", "r") as f:
    token = f.read().strip()

url = "https://reservar-pizza-162564426520.us-central1.run.app"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Payload ajustado para o formato esperado pela função (README 4.3)
pedidos = [
  {"order_id": "pedido-6c560222", "items": ["Guaraná 2L", "Borda Recheada"]},
  {"order_id": "pedido-589be6cf", "items": ["Pizza Portuguesa", "Borda Recheada", "Pizza Margherita"]},
  {"order_id": "pedido-322454e9", "items": ["Pizza Calabresa Família"]},
  {"order_id": "pedido-f1d4e631", "items": ["Pizza Margherita", "Pizza Calabresa Família", "Pizza Portuguesa"]},
  {"order_id": "pedido-4a30319a", "items": ["Pizza Portuguesa", "Borda Recheada", "Pizza Margherita"]},
  {"order_id": "pedido-e9262777", "items": ["Pizza Calabresa Família"]},
  {"order_id": "pedido-2acfc9fd", "items": ["Pizza Portuguesa", "Pizza Margherita"]},
  {"order_id": "pedido-1045badc", "items": ["Pizza Margherita", "Pizza Calabresa Família", "Guaraná 2L"]},
  {"order_id": "pedido-ee35b2a7", "items": ["Borda Recheada"]},
  {"order_id": "pedido-68c119f0", "items": ["Guaraná 2L"]}
]

for p in pedidos:
    print(f"Enviando pedido {p['order_id']}...")
    try:
        response = requests.post(url, json=p, headers=headers)
        print(f"Status: {response.status_code} - Resposta: {response.text}")
    except Exception as e:
        print(f"Erro: {e}")
