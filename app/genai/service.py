from app.guardrails.pii import mask_pii

def classify_intent(message: str) -> str:
    m=message.lower()
    if any(x in m for x in ["don't recognize","do not recognize","dispute","fraud"]): return "DISPUTE"
    if "transaction" in m: return "TRANSACTIONS"
    if any(x in m for x in ["balance","account"]): return "ACCOUNT"
    if "loan" in m: return "LOAN_INFO"
    if any(x in m for x in ["policy","how long","rule"]): return "POLICY"
    return "GENERAL"

def draft_response(text: str) -> str:
    return mask_pii(text)
