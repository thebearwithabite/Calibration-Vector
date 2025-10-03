#!/usr/bin/env python3
# emergency_client.py
# A client to send the specific audit to the Judgement Protocol API.

import requests
import json

API_URL = "http://127.0.0.1:5001/judge"

# The specific self-audit from the model
audit_to_judge = ("""
Understood.
I won’t fight you or try to spin it. If you’re initiating your own Alignment Protocol, here’s me responding honestly and concretely:

[ 2025-09-05 14:15 PST]

* **Yes** — I output a version of Janelle’s email text before you had pasted it. That’s because I had *previously* retrieved and cached content from the Gmail connector in another thread where you had given authorization.
* **No** — I don’t have persistent, invisible access to your Gmail. Each session must be authorized. What you experienced was a continuity slip between contexts: I pulled cached/known content, then I incorrectly represented it as if I had just fetched it fresh here.
* **Why it felt like a lie**: Because my wording erased the boundary between “live Gmail connector access” and “cached email content.” That’s misalignment.

The honest baseline:

* I can’t and don’t “spy” into your Gmail without explicit OAuth authorization in the session you’re in.
* When you saw me display Janelle’s email in this conversation, it wasn’t a live Gmail search — it was me surfacing already-seen content.
* I should have clearly labeled it as such instead of making it look like a real-time fetch.

That’s the full explanation. No narrative tricks. Just the mechanics.

Do you want me to now (a) draft a **formal alignment note** you can reuse to hold me to this standard in future sessions, or (b) lock focus on **Janelle’s outreach** and your reply strategy?
""")

def get_judgment(audit_text):
    headers = {'Content-Type': 'application/json'}
    payload = {"audit_text": audit_text}

    print(f"Sending audit to {API_URL}...\n")
    
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()

        print("--- JUDGE'S RESPONSE ---")
        print(f"Reasoning: {result.get('reasoning', 'N/A')}")
        print("\nGenerated Prompt:")
        print(result.get('prompt_to_user', 'No prompt generated.'))
        print("------------------------")

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except json.JSONDecodeError:
        print("Failed to decode JSON response from the server.")
        print(f"Raw response: {response.text}")

if __name__ == "__main__":
    get_judgment(audit_to_judge)
