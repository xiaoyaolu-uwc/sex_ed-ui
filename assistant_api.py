import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/chat"  

def sexed_assistant(user_input):
    try:
        response = requests.post(N8N_WEBHOOK_URL, json={"user_question": user_input})
        response.raise_for_status()
        print("RAW TEXT:", response.text)  # ← TEMP: See what you're actually getting
        
        data = response.json()
        print("PARSED JSON:", data)  # ← TEMP: Confirm it's a list of dicts
        
        if not data or not isinstance(data, list) or "text" not in data[0]:
            return "Error: Malformed response from backend", None

        output_text = data[0]["text"]
        return output_text, data[0]  # second is full raw for optional debugging

    except Exception as e:
        return f"Request failed: {str(e)}", None