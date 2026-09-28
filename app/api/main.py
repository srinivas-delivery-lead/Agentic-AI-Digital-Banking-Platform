from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.orchestrator import handle, AUDIT
from app.agents.loan_agents import kyc_agent, eligibility_agent, risk_agent, decision

app=FastAPI(title="BankAI Agentic Banking Demo",version="2.0.0")

class ChatRequest(BaseModel):
    customer_id:str="C1001"
    message:str
    human_approved:bool=False

class LoanRequest(BaseModel):
    customer_id:str="C1001"
    amount:float
    monthly_income:float
    monthly_obligations:float=0
    human_approved:bool=False

@app.get("/health")
def health(): return {"status":"ok","mode":"synthetic-demo","phases":["dispute","loan-origination"]}

@app.post("/chat")
def chat(req:ChatRequest): return handle(req.customer_id,req.message,req.human_approved)

@app.post("/loan/apply")
def loan(req:LoanRequest):
    # Synthetic customer fixture; production would retrieve an authorized customer profile.
    customer={"customer_id":req.customer_id,"kyc_status":"VERIFIED"}
    k=kyc_agent(customer)
    e=eligibility_agent(req.monthly_income,req.amount)
    r=risk_agent(req.monthly_income,req.monthly_obligations,req.amount)
    d=decision(req.human_approved,e["passed"],k["passed"],r["risk"])
    AUDIT.extend([
      {"agent":"KYCAgent","action":"verify_kyc","outcome":"PASS" if k["passed"] else "FAIL"},
      {"agent":"EligibilityAgent","action":"check_eligibility","outcome":"PASS" if e["passed"] else "FAIL"},
      {"agent":"RiskAgent","action":"assess_risk","outcome":r["risk"]},
      {"agent":"HumanApproval","action":"loan_decision","outcome":d["status"]}
    ])
    return {"workflow":"LOAN_ORIGINATION","kyc":k,"eligibility":e,"risk":r,"decision":d}

@app.get("/audit")
def audit(): return AUDIT
