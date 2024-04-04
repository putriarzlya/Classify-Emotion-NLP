"""
Putri Arzalya Maharani

Generating a dedicated file for invoking the utilized functions.
"""
import pandas as pd
import numpy as np
# preprocess
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from tensorflow.keras.models import load_model
import joblib

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
stopword_list= joblib.load('stopword_list.joblib')

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = text.lower() # lowercase text
    tokens = word_tokenize(text) # tokenize
    filtered_words = [word for word in tokens if word.lower() not in stopword_list]
    lemmatized_words = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in filtered_words]
    lemmatized_clean = [word.translate(str.maketrans('', '', string.punctuation)) for word in lemmatized_words]
    return ' '.join(lemmatized_clean)

def prediction(X):
    model = load_model('best_model.keras')
    y_pred = model.predict(X)
    predictions = np.argmax(y_pred, axis=1)
    for val in predictions:
        if val == 0:
            return 0, f"**Fear** is the emotion that you are currently feeling"
        elif val == 1:
            return 1, f"**Anger** is the emotion that you are currently feeling"
        else:
            return 2, f"**Joy** is the emotion that you are currently feeling"