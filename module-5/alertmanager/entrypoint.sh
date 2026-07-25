#!/bin/sh
set -e

echo "Generating Alertmanager config from environment variables..."

sed \
  -e "s|GMAIL_ADDRESS_PLACEHOLDER|${GMAIL_ADDRESS}|g" \
  -e "s|GMAIL_PASSWORD_PLACEHOLDER|${GMAIL_APP_PASSWORD}|g" \
  -e "s|SLACK_WARNING_PLACEHOLDER|${SLACK_WARNING_WEBHOOK}|g" \
  -e "s|SLACK_CRITICAL_PLACEHOLDER|${SLACK_CRITICAL_WEBHOOK}|g" \
  /etc/alertmanager/alertmanager.yml.template > /etc/alertmanager/alertmanager.yml

echo "Config generated. Starting Alertmanager..."
exec /bin/alertmanager \
  --config.file=/etc/alertmanager/alertmanager.yml \
  --storage.path=/alertmanager \
  --web.listen-address=:9093 \
  --log.level=info
