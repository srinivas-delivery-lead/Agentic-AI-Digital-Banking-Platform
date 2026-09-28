# Interview Guide — explain it simply

## 30-second answer
I built a synthetic digital-banking AI prototype to demonstrate the difference between Generative AI and Agentic AI. Generative AI understands customer language, retrieves policy knowledge and drafts responses. Agentic AI coordinates specialized agents that use controlled banking tools to complete multi-step workflows. For sensitive actions such as a high-value dispute, I added human approval and an audit trail.

## Explain like a school example
Think of the Supervisor Agent as a bank branch manager. The customer asks the manager a question. The manager decides which specialist should handle it. The Account Agent checks accounts, the Transaction Agent checks transactions, and the Dispute Agent handles suspicious transactions. The specialists cannot do anything they want; they use approved tools and important actions need a human manager's approval.

## 5-minute demo
1. Show README architecture.
2. Call `/health`.
3. Ask for recent transactions.
4. Ask to dispute `T9003` for INR 25,000.
5. Show `HUMAN_APPROVAL_REQUIRED`.
6. Repeat with `human_approved=true`.
7. Show generated case ID.
8. Open `/audit` and explain traceability.

## Questions interviewers may ask
**Why agentic AI?** Because the use case needs planning, tool use and coordination across steps, not only text generation.

**Why not let the LLM directly execute banking transactions?** A regulated workflow needs deterministic authorization, least privilege, approvals and auditability. The model proposes/coordinates; controlled services execute.

**Where is RAG?** The policy retriever grounds responses in curated synthetic banking policy documents. A production design could replace the simple retriever with embeddings/vector search plus document-level authorization.

**Is this production-ready?** No. It is a reference implementation. Production would require enterprise IAM, encryption/key management, real API contracts, model governance, monitoring, prompt-injection defenses, privacy controls, DR, penetration testing and regulatory validation.

## Your role positioning
Describe yourself as the solution/delivery owner who defined the banking use case, decomposed the workflow, designed controls and acceptance criteria, coordinated the AI/API architecture, and built a prototype to deepen technical fluency. Do not claim that this demo is a deployed bank production system.
