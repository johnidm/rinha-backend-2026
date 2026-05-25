# Rinha de Backend 2026 — Detecção de Fraude com Busca Vetorial



> http://0.0.0.0:9999/schema/swagger

## Build & deploy local (Docker)

```bash
make up # nginx + api-1 + api-2
```

Home: `curl -i http://localhost:9999`

Healthcheck: `curl -i http://localhost:9999/ready`.

Exemplo de chamada:

```bash
curl -s -X POST http://localhost:9999/fraud-score \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "tx-123",
    "transaction": {"amount": 384.88, "installments": 3, "requested_at": "2026-03-11T20:23:35Z"},
    "customer": {"avg_amount": 769.76, "tx_count_24h": 3, "known_merchants": ["MERC-001"]},
    "merchant": {"id": "MERC-001", "mcc": "5912", "avg_amount": 298.95},
    "terminal": {"is_online": false, "card_present": true, "km_from_home": 13.7},
    "last_transaction": {"timestamp": "2026-03-11T14:58:35Z", "km_from_current": 18.8}
  }'
```

## Teste the image 

```bash
docker run -p 9999:9999 ghcr.io/johnidm/rinha-backend-2026:latest
```
