SENSITIVE_ACTIONS = {"create_dispute", "block_card", "transfer_funds"}

def approval_required(action: str, amount: float = 0) -> bool:
    if action in {"block_card", "transfer_funds"}: return True
    return action == "create_dispute" and amount >= 10000
