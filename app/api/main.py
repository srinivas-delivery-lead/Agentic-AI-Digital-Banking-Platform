from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.orchestrator import handle, AUDIT
app=FastAPI(title="BankAI Agentic Banking Demo",version="1.0.0")
class ChatRequest(BaseModel):
    customer_id:str="C1001"
    message:str
    human_approved:bool=False
@app.get("/health")
def health(): return {"status":"ok","mode":"synthetic-demo"}
@app.post("/chat")
def chat(req:ChatRequest): return handle(req.customer_id,req.message,req.human_approved)
@app.get("/audit")
def audit(): return AUDIT
