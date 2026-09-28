from app.agents.loan_agents import kyc_agent, eligibility_agent, risk_agent, decision

def test_loan_agents_and_human_gate():
    assert kyc_agent({"kyc_status":"VERIFIED"})["passed"]
    assert eligibility_agent(100000,500000)["passed"]
    r=risk_agent(100000,20000,500000)
    assert r["risk"]=="LOW"
    assert decision(False,True,True,r["risk"])["status"]=="HUMAN_APPROVAL_REQUIRED"
    assert decision(True,True,True,r["risk"])["status"]=="APPROVED"
