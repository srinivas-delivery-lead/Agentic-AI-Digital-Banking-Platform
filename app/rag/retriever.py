from pathlib import Path
KB=Path(__file__).resolve().parents[2]/"knowledge-base"

def retrieve(query: str) -> str:
    file="loan_policy.md" if "loan" in query.lower() else "dispute_policy.md"
    return (KB/file).read_text()
