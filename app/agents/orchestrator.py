import re, uuid
from datetime import datetime, timezone
from app.genai.service import classify_intent, draft_response
from app.rag.retriever import retrieve
from app.guardrails.policy import approval_required
from importlib import import_module
bank=import_module("mock_banking_api.service")
AUDIT=[]

def _audit(agent, action, outcome, reason=""):
    AUDIT.append({"time":datetime.now(timezone.utc).isoformat(),"agent":agent,"action":action,"outcome":outcome,"reason":reason})

def handle(customer_id: str, message: str, human_approved: bool=False):
    intent=classify_intent(message); _audit("Supervisor","classify_intent",intent)
    if intent == "ACCOUNT":
        data=bank.accounts_for(customer_id); _audit("AccountAgent","get_accounts","SUCCESS")
        return {"intent":intent,"response":draft_response(f"Account summary: {data}"),"data":data,"audit":AUDIT[-2:]}
    if intent == "TRANSACTIONS":
        data=bank.transactions_for(customer_id); _audit("TransactionAgent","get_transactions","SUCCESS")
        return {"intent":intent,"response":"Here are your synthetic recent transactions.","data":data,"audit":AUDIT[-2:]}
    if intent == "DISPUTE":
        match=re.search(r"T\d+", message.upper()); txid=match.group(0) if match else "T9003"
        tx=bank.transaction(customer_id,txid); _audit("TransactionAgent","get_transaction","SUCCESS" if tx else "NOT_FOUND")
        if not tx: return {"intent":intent,"response":"Transaction not found.","audit":AUDIT[-2:]}
        if approval_required("create_dispute",tx["amount"]) and not human_approved:
            _audit("FraudDisputeAgent","approval_gate","PENDING",f"Amount INR {tx['amount']}")
            return {"intent":intent,"status":"HUMAN_APPROVAL_REQUIRED","transaction":tx,"response":"I found the transaction. A human approval is required before this demo can create the dispute.","audit":AUDIT[-3:]}
        case="D-"+uuid.uuid4().hex[:8].upper(); _audit("FraudDisputeAgent","create_dispute","SUCCESS",case)
        return {"intent":intent,"status":"DISPUTE_CREATED","case_id":case,"transaction":tx,"response":f"Synthetic dispute {case} has been created.","audit":AUDIT[-3:]}
    if intent in {"POLICY","LOAN_INFO"}:
        context=retrieve(message); _audit("CustomerServiceAgent","retrieve_policy","SUCCESS")
        return {"intent":intent,"response":context,"audit":AUDIT[-2:]}
    _audit("CustomerServiceAgent","general_response","SUCCESS")
    return {"intent":intent,"response":"I can help with accounts, transactions, disputes and sample loan/policy questions.","audit":AUDIT[-2:]}
