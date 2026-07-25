# Observability Lab

A production-grade observability stack built from scratch across six modules.
Documented publicly as part of an observability customisation role assignment.

## Stack

| Component | Purpose | Module |
|-----------|---------|--------|
| Prometheus | Metrics collection and alerting | 1, 2 |
| Grafana | Unified visualisation | 1, 3 |
| Loki | Log aggregation | 4 |
| Promtail | Log shipping agent | 4 |
| Alertmanager | Alert routing — Slack, email, webhook | 5 |
| Tempo | Distributed trace storage | 6 |
| OpenTelemetry | Trace instrumentation and collection | 6 |

## Three Pillars

| Pillar | Tool | Question answered |
|--------|------|------------------|
| Metrics | Prometheus | WHAT is happening |
| Logs | Loki | WHY it happened |
| Traces | Tempo | WHERE exactly it broke |

## Structure

observability-lab/
├── module-1/ # Prometheus + Grafana basics + first PromQL
├── module-2/ # Recording rules + alerting rules + hot-reload
├── module-3/ # Grafana dashboards as code + provisioning
├── module-4/ # Loki + Promtail + LogQL log aggregation
├── module-5/ # Alertmanager — Slack, email, webhook routing
└── module-6/ # Tempo + OpenTelemetry distributed traces


## Running any module

```bash
cd module-N
docker compose up -d
docker compose ps
```

## Key concepts covered

- PromQL — metrics querying and aggregation
- Recording rules — pre-computing expensive queries
- Alert rules — threshold-based alerting with for durations
- Grafana provisioning — dashboards and datasources as code
- Label cardinality — designing Loki labels correctly
- LogQL — log filtering, JSON parsing, numeric comparisons
- Alertmanager routing — severity-based alert routing
- Inhibition rules — suppressing noise during incidents
- Credential security — entrypoint scripts, env files, gitignore
- Distributed traces — spans, trace IDs, waterfall diagrams
- Cross-pillar correlation — logs to traces to metrics

## Blog series

Full documentation of every module published on Hashnode.
Every config file explained. Every error debugged. Every lesson documented.

## Modules completed

- [x] Module 0 — Environment setup
- [x] Module 1 — First metrics stack
- [x] Module 2 — Prometheus deep control
- [x] Module 3 — Grafana as code
- [x] Module 4 — Log aggregation
- [x] Module 5 — Alertmanager
- [x] Module 6 — Distributed traces
