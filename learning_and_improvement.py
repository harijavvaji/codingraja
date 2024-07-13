def collect_feedback(user_input, chatbot_response, feedback):
    # Store feedback for future training
    with open('feedback.csv', 'a') as f:
        f.write(f"{user_input},{chatbot_response},{feedback}\n")

# Example usage
user_input = "Hi"
chatbot_response = "Hello! How can I help you today?"
feedback = "positive"
collect_feedback(user_input, chatbot_response, feedback)
