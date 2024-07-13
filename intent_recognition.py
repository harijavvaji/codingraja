from text_preprocessing import preprocess_text

intents = {
    "greeting": ["hello", "hi", "hey"],
    "weather": ["weather", "temperature", "forecast"]
}

def recognize_intent(text):
    tokens = preprocess_text(text)
    for intent, keywords in intents.items():
        if any(word in tokens for word in keywords):
            return intent
    return "unknown"

# Example usage
user_input = "Hi, how are you?"
intent = recognize_intent(user_input)
print(intent)
