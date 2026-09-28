# Phase 2 — Agentic Loan Origination

## Business journey
Customer applies for a synthetic personal loan → KYC Agent → Eligibility Agent → Risk Agent → Human Approval → Decision/Notification.

## Why this is Agentic AI
The workflow is decomposed into specialist responsibilities. An orchestrator calls agents/tools in sequence, preserves state, stops on policy failures and requires human authorization before a final simulated credit decision.

## Controls
- No real credit bureau or bank integration
- No real customer data
- Deterministic eligibility/risk rules for explainability
- Human-in-the-loop final decision
- Audit events for every stage
- GenAI may summarize/explain but does not override policy

## Interview demo
Submit INR 500,000 with monthly income INR 100,000 and obligations INR 20,000. Show KYC PASS, eligibility PASS, LOW risk, then HUMAN_APPROVAL_REQUIRED. Repeat with approval enabled and show the simulated decision and application ID.
