import requests

N8N_WEBHOOK_URL = "https://abc123.ngrok.io/webhook/chat"  # replace with yours

def sexed_assistant(user_input):
    try:
        response = requests.post(N8N_WEBHOOK_URL, json={"user_question": user_input})
        response.raise_for_status()
        data = response.json()
        
        if not data or not isinstance(data, list) or "output" not in data[0]:
            return "Error: Malformed response from backend", None

        output_text = data[0]["output"]
        return output_text, data[0]  # second is full raw for optional debugging

    except Exception as e:
        return f"Request failed: {str(e)}", None