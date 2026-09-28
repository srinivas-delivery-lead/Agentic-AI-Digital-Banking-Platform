import json
from pathlib import Path
BASE = Path(__file__).resolve().parents[1] / "sample-data"

def _load(name): return json.loads((BASE/name).read_text())
def accounts_for(customer_id): return [x for x in _load("accounts.json") if x["customer_id"] == customer_id]
def transactions_for(customer_id):
    ids={x["account_id"] for x in accounts_for(customer_id)}
    return [x for x in _load("transactions.json") if x["account_id"] in ids]
def transaction(customer_id, transaction_id): return next((x for x in transactions_for(customer_id) if x["transaction_id"] == transaction_id), None)
