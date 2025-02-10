# api key app-9wDu4ap97skBFe2kt37MWD4S

```bash
curl -X POST 'http://192.168.127.146/v1/workflows/run' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "response_mode": "streaming",
    "user": "abc-123"
}'
```

```bash
curl -X POST 'http://192.168.127.146/v1/workflows/run' \
--header 'Authorization: Bearer app-9wDu4ap97skBFe2kt37MWD4S' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {a:1,b:2,c:3},
    "response_mode": "streaming",
    "user": "harry"
}'
```

``json
{
    "workflow_run_id": "djflajgkldjgd",
    "task_id": "9da23599-e713-473b-982c-4328d4f5c78a",
    "data": {
        "id": "fdlsjfjejkghjda",
        "workflow_id": "fldjaslkfjlsda",
        "status": "succeeded",
        "outputs": {
          "text": "Nice to meet you."
        },
        "error": null,
        "elapsed_time": 0.875,
        "total_tokens": 3562,
        "total_steps": 8,
        "created_at": 1705407629,
        "finished_at": 1727807631
    }
}
```

