import requests
import json

with open("token.txt", "r") as f:
    token = f.read().strip()

url = "https://reservar-pizza-162564426520.us-central1.run.app"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

pedidos = [
  {"order": {"id": "pedido-6c560222", "amount": 53.87, "customer": "João Silva", "items": ["Guaraná 2L", "Borda Recheada"]}},
  {"order": {"id": "pedido-589be6cf", "amount": 94.28, "customer": "Carlos Pereira", "items": ["Pizza Portuguesa", "Borda Recheada", "Pizza Margherita"]}},
  {"order": {"id": "pedido-322454e9", "amount": 80.28, "customer": "Maria Souza", "items": ["Pizza Calabresa Família"]}},
  {"order": {"id": "pedido-f1d4e631", "amount": 88.26, "customer": "Maria Souza", "items": ["Pizza Margherita", "Pizza Calabresa Família", "Pizza Portuguesa"]}},
  {"order": {"id": "pedido-4a30319a", "amount": 84.95, "customer": "Ana Oliveira", "items": ["Pizza Portuguesa", "Borda Recheada", "Pizza Margherita"]}},
  {"order": {"id": "pedido-e9262777", "amount": 59.52, "customer": "João Silva", "items": ["Pizza Calabresa Família"]}},
  {"order": {"id": "pedido-2acfc9fd", "amount": 25.94, "customer": "Ana Oliveira", "items": ["Pizza Portuguesa", "Pizza Margherita"]}},
  {"order": {"id": "pedido-1045badc", "amount": 87.48, "customer": "Carlos Pereira", "items": ["Pizza Margherita", "Pizza Calabresa Família", "Guaraná 2L"]}},
  {"order": {"id": "pedido-ee35b2a7", "amount": 33.61, "customer": "João Silva", "items": ["Borda Recheada"]}},
  {"order": {"id": "pedido-68c119f0", "amount": 55.11, "customer": "Carlos Pereira", "items": ["Guaraná 2L"]}}
]

for p in pedidos:
    print(f"Enviando pedido {p['order']['id']}...")
    try:
        response = requests.post(url, json=p, headers=headers)
        print(f"Status: {response.status_code} - Resposta: {response.text}")
    except Exception as e:
        print(f"Erro: {e}")
