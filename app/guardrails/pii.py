import re

def mask_pii(text: str) -> str:
    text = re.sub(r"\b\d{10}\b", "[MASKED_MOBILE]", text)
    text = re.sub(r"\b\d{12}\b", "[MASKED_ID]", text)
    return text
