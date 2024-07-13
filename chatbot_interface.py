from flask import Flask, render_template, request, jsonify
from intent_recognition_spacy import recognize_intent_spacy
from response_generation import generate_response

app = Flask(__name__, template_folder='templates')

# Route to render the index.html file
@app.route('/')
def index():
    # Greeting message and options
    greeting_message = "Hello! How can I help you?"
    options = ["coding raja", "chatbot project"]
    return render_template('index.html', message=greeting_message, options=options)

# Route to handle POST requests to /chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    
    # Recognize intent
    intent = recognize_intent_spacy(message)
    
    # Generate response based on intent
    response = generate_response(intent)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
