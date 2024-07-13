import nltk # type: ignore
from nltk.corpus import stopwords # type: ignore
from nltk.tokenize import word_tokenize # type: ignore
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return tokens

# Example usage
sample_text = "Hi, how are you?"
cleaned_text = preprocess_text(sample_text)
print(cleaned_text)
