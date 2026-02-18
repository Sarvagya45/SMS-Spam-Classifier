import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

ps = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

def transform_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)

    # remove non-alphanumeric
    y = []
    for x in tokens:
        if x.isalnum():
            y.append(x)

    # remove stopwords and punctuation
    filtered = []
    for i in y:
        if i not in stopwords.words('english') and i not in string.punctuation:
            filtered.append(i)

    # stemming
    stemmed = []
    for i in filtered:
        stemmed.append(ps.stem(i))

    return " ".join(stemmed)

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1.preprocess
    transformed_sms = transform_text(input_sms)
    # 2.vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3.predict
    result = model.predict(vector_input)[0]
    # Display
    if result == 1:
        st.header("Spam Detected")
    else:
        st.header("No Spam Detected")