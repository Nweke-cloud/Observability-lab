#!/usr/bin/env python3
import time
import random
import requests
from datetime import datetime

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

resource = Resource.create({
    "service.name": "sample-app",
    "service.version": "1.0.0",
    "deployment.environment": "lab"
})

provider = TracerProvider(resource=resource)
exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)
processor = BatchSpanProcessor(exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("sample-app")

SERVICES = ["api-gateway", "auth-service", "payment-service", "user-service"]

def simulate_db_call(service_name, operation):
    with tracer.start_as_current_span(f"{service_name}.db.{operation}") as span:
        latency = random.uniform(0.05, 2.0)
        span.set_attribute("db.system", "postgresql")
        span.set_attribute("db.operation", operation)
        span.set_attribute("db.latency_ms", round(latency * 1000))
        if latency > 1.5:
            span.set_attribute("error", True)
            span.set_attribute("error.message", "Query timeout exceeded threshold")
        time.sleep(latency)
        return latency

def simulate_service_call(service_name):
    with tracer.start_as_current_span(f"{service_name}.process") as span:
        span.set_attribute("service.name", service_name)
        span.set_attribute("http.method", "POST")
        span.set_attribute("http.url", f"http://{service_name}/api/v1/process")

        db_latency = simulate_db_call(service_name, "SELECT")
        total = db_latency + random.uniform(0.01, 0.1)

        span.set_attribute("http.status_code", 500 if db_latency > 1.5 else 200)
        span.set_attribute("duration_ms", round(total * 1000))
        return total

def simulate_request():
    request_id = f"req-{random.randint(10000, 99999)}"
    service = random.choice(SERVICES)

    with tracer.start_as_current_span("http.request") as span:
        span.set_attribute("http.method", "POST")
        span.set_attribute("request.id", request_id)
        span.set_attribute("service.target", service)

        total = simulate_service_call(service)
        status = "error" if total > 1.5 else "success"
        span.set_attribute("request.status", status)
        span.set_attribute("request.duration_ms", round(total * 1000))

        print(f"{datetime.now().strftime('%H:%M:%S')} | {service} | {status} | {round(total*1000)}ms")

print("Sample app started. Generating traces every 2 seconds...")
print("Sending to otel-collector:4317")
print("-" * 50)

while True:
    try:
        simulate_request()
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
