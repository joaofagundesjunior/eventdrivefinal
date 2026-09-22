import functions_framework
import base64
import json
import os

def log_event(message, severity="INFO", trace_context=None):
    project_id = os.environ.get("PROJECT_ID")
    
    log_entry = {
        "message": message,
        "severity": severity
    }

    # Para eventos Pub/Sub, o trace context pode vir nos atributos da mensagem
    # ou podemos tentar extrair se estiver disponível no cloud_event.
    # Como o Workflow publica no Pub/Sub, ele pode não passar o trace header automaticamente
    # a menos que configurado. Mas o Cloud Functions 2nd gen injeta trace no contexto.
    
    # Se tivéssemos o trace_id, usaríamos:
    # log_entry["logging.googleapis.com/trace"] = f"projects/{project_id}/traces/{trace_id}"

    print(json.dumps(log_entry))

@functions_framework.cloud_event
def dead_letter(cloud_event):
    # Processa falhas vindas do Pub/Sub DLQ
    try:
        data_payload = base64.b64decode(cloud_event.data["message"]["data"]).decode()
        log_event(f"Falha detectada no processamento: {data_payload}", severity="WARNING")
    except Exception as e:
        log_event(f"Erro ao processar DLQ: {e}", severity="ERROR")
