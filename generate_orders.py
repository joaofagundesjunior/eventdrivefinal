import random
import time
import uuid
import json

# Lista de opções para gerar pedidos aleatórios
pizzas = ["Pizza Calabresa Família", "Borda Recheada", "Guaraná 2L", "Pizza Margherita", "Pizza Portuguesa"]
clientes = ["João Silva", "Maria Souza", "Carlos Pereira", "Ana Oliveira"]

def gerar_pedido():
    order_id = str(uuid.uuid4())[:8]
    item_count = random.randint(1, 3)
    items = random.sample(pizzas, item_count)
    amount = round(random.uniform(20.0, 100.0), 2)
    
    pedido = {
        "order": {
            "id": f"pedido-{order_id}",
            "amount": amount,
            "customer": random.choice(clientes),
            "items": items
        }
    }
    return pedido

def main():
    total_pedidos = 0
    limite_pedidos = 100

    print(f"Iniciando gerador de pedidos (Limite: {limite_pedidos})...")

    try:
        while total_pedidos < limite_pedidos:
            num_pedidos_neste_ciclo = random.randint(1, 3)
            
            for _ in range(num_pedidos_neste_ciclo):
                if total_pedidos >= limite_pedidos:
                    break
                
                pedido = gerar_pedido()
                print(f"Pedido #{total_pedidos + 1} realizado: {json.dumps(pedido, ensure_ascii=False)}")
                
                # Aqui você poderia adicionar o código para postar no Workflow ou endpoint
                # requests.post(url, json=pedido)
                
                total_pedidos += 1
            
            if total_pedidos >= limite_pedidos:
                break
                
            print(f"Aguardando 60 segundos antes do próximo ciclo ({total_pedidos} pedidos feitos)...")
            time.sleep(60)

    except KeyboardInterrupt:
        print("\nScript parado manualmente.")
    
    print(f"Gerador encerrado. Total de pedidos: {total_pedidos}")

if __name__ == "__main__":
    main()
