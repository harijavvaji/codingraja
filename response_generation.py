responses = {
    "greeting": "Hello! How can I help you today?",
    "weather": "It's sunny and warm today.",
    "unknown": "I'm sorry, I didn't understand that."
}

def generate_response(intent):
    return responses.get(intent, responses["unknown"])

# Example usage
intent = "greeting"
response = generate_response(intent)
print(response)
