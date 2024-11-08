import json
import requests
from typing import Optional, Tuple

# Configuration
BASE_API_URL = "http://192.168.127.134:7860"
FLOW_ID = "6bd4d148-969b-4cb6-933b-7583da515d14"  # Replace with your specific flow ID
TWEAKS = {
  "ChatInput-DtEC4": {},
  "Prompt-jldPr": {},
  "ChatOutput-45bZS": {},
  "OpenAIModel-kRcPr": {},
  "None-jCX7Q": {}
}

def run_flow(message: str, session_id: Optional[str] = None) -> Tuple[dict, Optional[str]]:
    """
    Sends a message to the flow and returns the response and session ID.

    :param message: The message to send to the flow.
    :param session_id: The session ID for maintaining the conversation.
    :return: A tuple with the JSON response and session ID.
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{FLOW_ID}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": TWEAKS
    }
    if session_id:
        payload["session_id"] = session_id  # Maintain the conversation session

    response = requests.post(api_url, json=payload)
    response_data = response.json()
    
    if "session_id" in response_data:
        session_id = response_data["session_id"]
    
    return response_data, session_id


def main():
    # Starting a new conversation
    session_id = None
    messages = [
        "Why is the sky blue?",
        "Can you tell me a joke?",
        "What's the weather like today?",
        "Thank you!"
    ]

    for message in messages:
        response_data, session_id = run_flow(message, session_id)
        
        # Extract and print the AI's response from nested JSON
        try:
            ai_response = response_data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
            print(f"User: {message}")
            print(f"AI: {ai_response}\n")
        except (KeyError, IndexError, TypeError) as e:
            print("Error extracting AI response:", e)
            print("Full response data:", json.dumps(response_data, indent=2))
            break

if __name__ == "__main__":
    main()
