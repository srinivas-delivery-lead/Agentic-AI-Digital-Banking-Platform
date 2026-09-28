# Solution Architecture

```mermaid
flowchart TB
UI[Customer UI] --> API[FastAPI Gateway]
API --> SEC[PII Masking & Guardrails]
SEC --> SUP[Supervisor Agent]
SUP --> RAG[Policy Retrieval]
SUP --> ACCT[Account Agent]
SUP --> TX[Transaction Agent]
SUP --> FD[Fraud/Dispute Agent]
FD --> HITL[Human-in-the-loop]
ACCT --> CORE[Mock Core Banking]
TX --> CORE
FD --> CORE
SUP --> AUDIT[Audit Log]
```

The LLM/GenAI layer does not directly own privileged banking operations. Agents can call only approved tools, and sensitive workflows pass through deterministic policy controls.
