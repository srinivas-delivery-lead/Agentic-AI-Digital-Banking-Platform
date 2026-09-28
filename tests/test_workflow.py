from app.agents.orchestrator import handle

def test_high_value_dispute_needs_approval():
    r=handle("C1001","I don't recognize transaction T9003. Raise a dispute.")
    assert r["status"] == "HUMAN_APPROVAL_REQUIRED"

def test_approved_dispute_creates_case():
    r=handle("C1001","Dispute T9003",True)
    assert r["status"] == "DISPUTE_CREATED"
