import functions_framework
import json
import os

def log_event(message, request, severity="INFO"):
    project_id = os.environ.get("PROJECT_ID")
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    
    log_entry = {
        "message": message,
        "severity": severity
    }

    if trace_header:
        trace_parts = trace_header.split("/")
        trace_id = trace_parts[0]
        span_id = trace_parts[1].split(";")[0] if len(trace_parts) > 1 else None
        
        log_entry["logging.googleapis.com/trace"] = f"projects/{project_id}/traces/{trace_id}"
        if span_id:
            log_entry["logging.googleapis.com/spanId"] = span_id

    print(json.dumps(log_entry))

@functions_framework.http
def cobrar_pagamento(request):
    request_json = request.get_json(silent=True)
    idempotency_key = request.headers.get('Idempotency-Key')
    api_key = os.environ.get('PAYMENT_API_KEY', 'NOT_SET')
    
    if not request_json or 'amount' not in request_json:
        log_event("Erro: valor ausente na cobrança", request, severity="ERROR")
        return json.dumps({"error": "Missing amount"}), 400
    
    log_event(f"Processando pagamento de R${request_json['amount']} com chave {idempotency_key}", request)
    return json.dumps({"status": "paid", "transaction_id": "tx_12345"}), 200
