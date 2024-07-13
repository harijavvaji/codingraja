import spacy # type: ignore

# Load pre-trained spaCy model
nlp = spacy.load('en_core_web_sm')

def recognize_intent_spacy(text):
    doc = nlp(text)
    if "weather" in text:
        return "weather"
    return "unknown"

# Example usage
if __name__ == "__main__":
    user_input = "What's the weather like?"
    intent = recognize_intent_spacy(user_input)
    print(intent)
