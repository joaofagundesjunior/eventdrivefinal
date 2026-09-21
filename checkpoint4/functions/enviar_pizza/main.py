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
def enviar_pizza(request):
    request_json = request.get_json(silent=True)
    order_id = request_json.get('order_id') if request_json else 'desconhecido'
    
    log_event(f"Enviando pizza para o pedido {order_id}", request)
    return json.dumps({"status": "shipped", "order_id": order_id, "tracking_id": "track_98765"}), 200
