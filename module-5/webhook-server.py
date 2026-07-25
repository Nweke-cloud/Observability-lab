#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        data = json.loads(body)
        print(f"\n{'='*60}")
        print(f"ALERT RECEIVED: {datetime.now().strftime('%H:%M:%S')}")
        print(f"Status: {data.get('status', 'unknown').upper()}")
        print(f"Receiver: {data.get('receiver', 'unknown')}")
        for alert in data.get('alerts', []):
            print(f"\n  Alert: {alert['labels'].get('alertname', 'unknown')}")
            print(f"  Severity: {alert['labels'].get('severity', 'unknown')}")
            print(f"  Instance: {alert['labels'].get('instance', 'unknown')}")
            print(f"  State: {alert.get('status', 'unknown')}")
            if 'annotations' in alert:
                print(f"  Description: {alert['annotations'].get('description', '')}")
        print(f"{'='*60}\n")
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass

print("Webhook server running on port 5001")
print("Waiting for Alertmanager notifications...")
HTTPServer(('0.0.0.0', 5001), WebhookHandler).serve_forever()
