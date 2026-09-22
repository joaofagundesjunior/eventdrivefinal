import requests
import json
import random
import uuid

with open("token.txt", "r") as f:
    token = f.read().strip()

url = "https://reservar-pizza-162564426520.us-central1.run.app"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

pizzas = ["Pizza Calabresa Família", "Borda Recheada", "Guaraná 2L", "Pizza Margherita", "Pizza Portuguesa"]

for _ in range(10):
    order_id = f"pedido-{str(uuid.uuid4())[:8]}"
    items = random.sample(pizzas, random.randint(1, 3))
    payload = {"order_id": order_id, "items": items}
    
    print(f"Enviando {order_id}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status: {response.status_code} - Resposta: {response.text}")
    except Exception as e:
        print(f"Erro ao enviar {order_id}: {e}")
