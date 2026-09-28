import streamlit as st, requests
st.set_page_config(page_title="BankAI",page_icon="🏦",layout="wide")
st.title("🏦 BankAI — GenAI + Agentic AI Banking Demo")
st.caption("Synthetic portfolio demo — no real banking connection")
customer=st.sidebar.text_input("Customer ID","C1001")
approved=st.sidebar.checkbox("Human approval granted")
msg=st.text_area("Ask BankAI","I don't recognize transaction T9003. Raise a dispute.")
if st.button("Run AI workflow"):
    try:
        r=requests.post("http://127.0.0.1:8000/chat",json={"customer_id":customer,"message":msg,"human_approved":approved},timeout=10)
        st.json(r.json())
    except Exception as e: st.error(f"Start the FastAPI service first: {e}")
