import tensorflow as tf # type: ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Embedding, LSTM, Dense # type: ignore

# Example data
conversations = [
    ("Hi", "Hello!"),
    ("How are you?", "I'm fine, thank you."),
    ("What's the weather like?", "It's sunny today.")
]

# Tokenization
tokenizer = Tokenizer()
all_sentences = [item for sublist in conversations for item in sublist]
tokenizer.fit_on_texts(all_sentences)
word_index = tokenizer.word_index

# Prepare sequences
input_texts, target_texts = zip(*conversations)
input_sequences = tokenizer.texts_to_sequences(input_texts)
target_sequences = tokenizer.texts_to_sequences(target_texts)
input_sequences = pad_sequences(input_sequences, padding='post')
target_sequences = pad_sequences(target_sequences, padding='post')

# Define model
model = Sequential()
model.add(Embedding(input_dim=len(word_index) + 1, output_dim=64, input_length=input_sequences.shape[1]))
model.add(LSTM(64, return_sequences=True))
model.add(LSTM(64))
model.add(Dense(len(word_index) + 1, activation='softmax'))

# Compile and train model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(input_sequences, target_sequences, epochs=10)

# Example inference
def generate_response_seq2seq(input_text):
    input_seq = tokenizer.texts_to_sequences([input_text])
    input_seq = pad_sequences(input_seq, maxlen=input_sequences.shape[1], padding='post')
    predicted_seq = model.predict(input_seq)
    response = tokenizer.sequences_to_texts(predicted_seq)
    return response[0]

# Example usage
if __name__ == "__main__":
    response = generate_response_seq2seq("Hi")
    print(response)
