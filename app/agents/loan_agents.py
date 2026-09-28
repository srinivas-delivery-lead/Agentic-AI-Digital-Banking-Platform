import uuid

def kyc_agent(customer):
    ok=customer.get("kyc_status")=="VERIFIED"
    return {"agent":"KYCAgent","passed":ok,"reason":"KYC verified" if ok else "KYC review required"}

def eligibility_agent(monthly_income, amount):
    passed=monthly_income>=50000 and amount<=monthly_income*12
    return {"agent":"EligibilityAgent","passed":passed,"reason":"Synthetic income/amount rules passed" if passed else "Outside synthetic eligibility rules"}

def risk_agent(monthly_income, monthly_obligations, amount):
    ratio=round(monthly_obligations/monthly_income,2) if monthly_income else 1
    risk="LOW" if ratio<=0.35 and amount<=monthly_income*10 else "MEDIUM" if ratio<=0.5 else "HIGH"
    return {"agent":"RiskAgent","risk":risk,"obligation_ratio":ratio,"requires_human_approval":True}

def decision(human_approved, eligible, kyc_ok, risk):
    if not human_approved: return {"status":"HUMAN_APPROVAL_REQUIRED"}
    approved=eligible and kyc_ok and risk!="HIGH"
    return {"status":"APPROVED" if approved else "DECLINED","application_id":"L-"+uuid.uuid4().hex[:8].upper()}
