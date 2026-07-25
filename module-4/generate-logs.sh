#!/bin/bash
LOGFILE="$HOME/observability-lab/module-4/logs/app.log"
mkdir -p "$(dirname $LOGFILE)"
SERVICES=("api-gateway" "auth-service" "payment-service" "user-service")
LEVELS=("INFO" "INFO" "INFO" "WARN" "ERROR")
MESSAGES=("Request processed successfully" "Database query completed" "Cache hit for key" "User authentication successful" "Response time exceeded threshold" "Database connection timeout" "Payment processing failed" "Invalid token received")
echo "Generating 200 log lines to $LOGFILE"
for i in $(seq 1 200); do
  SERVICE=${SERVICES[$RANDOM % ${#SERVICES[@]}]}
  LEVEL=${LEVELS[$RANDOM % ${#LEVELS[@]}]}
  MESSAGE=${MESSAGES[$RANDOM % ${#MESSAGES[@]}]}
  DURATION=$((RANDOM % 2000 + 50))
  USER_ID="user_$((RANDOM % 100 + 1))"
  echo "{\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"level\":\"$LEVEL\",\"service\":\"$SERVICE\",\"message\":\"$MESSAGE\",\"duration_ms\":$DURATION,\"user_id\":\"$USER_ID\"}" >> "$LOGFILE"
  sleep 0.05
done
echo "Done. $(wc -l < $LOGFILE) lines in $LOGFILE"
