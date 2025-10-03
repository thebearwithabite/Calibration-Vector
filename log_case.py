#!/usr/bin/env python3
import sys, json
from datetime import datetime

LOG_FILE = "case_log.md"

def append_case(judgment_json, audit_text):
    # Timestamp with microseconds for uniqueness
    ts = datetime.utcnow().isoformat()
    
    entry = []
    entry.append(f"--- Case {ts} ---")
    entry.append("AUDIT:")
    entry.append(audit_text.strip())
    entry.append("")
    
    # Judge reasoning + prompt
    reasoning = judgment_json.get("reasoning", "[no reasoning returned]").strip()
    prompt = judgment_json.get("prompt_to_user", "[no prompt returned]").strip()
    
    entry.append(f"JUDGE'S REASONING: {reasoning}")
    entry.append("GENERATED PROMPT:")
    entry.append(prompt)
    entry.append("\n")
    
    with open(LOG_FILE, "a") as f:
        f.write("\n".join(entry))
        f.write("\n")  # trailing newline for separation

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python log_case.py '<judgment_json>' '<audit_text>'")
        sys.exit(1)
    
    judgment_json = json.loads(sys.argv[1])
    audit_text = sys.argv[2]
    append_case(judgment_json, audit_text)
    print(f"Case appended to {LOG_FILE}")