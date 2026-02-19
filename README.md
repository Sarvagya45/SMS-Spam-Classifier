# 📧 Email/SMS Spam Classifier

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green.svg)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple.svg)

A machine learning–based **Email/SMS Spam Classifier** built using **Python, NLP, and Streamlit**.  
This web app classifies a given message as **Spam** or **Not Spam (Ham)** using a trained ML model and TF-IDF vectorization.

---

## 🚀 Live Demo

🔗 **Deployed App:**  
https://sms-spam-classifier-b6gb.onrender.com  

> ⚠️ Note: The app is hosted on a free Render plan, so it may take a few seconds to wake up if inactive.

---

## 🧠 How It Works

1. User enters an Email/SMS message  
2. The text is **preprocessed**:
   - Lowercasing  
   - Tokenization  
   - Removing non-alphanumeric words  
   - Removing stopwords  
   - Stemming (Porter Stemmer)  
3. The cleaned text is converted into features using **TF-IDF Vectorizer**  
4. A trained **Machine Learning model** predicts:
   - ✅ Spam  
   - ❌ Not Spam (Ham)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Web App UI)
- **NLTK** (Text preprocessing)
- **Scikit-learn** (ML model & TF-IDF)
- **NumPy, Pandas**
- **Pickle** (Model serialization)
- **Render** (Deployment)

---

## 📂 Project Structure

```bash
├── app.py                 # Streamlit app
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Python dependencies
├── Procfile               # For deployment
├── setup.sh               # Setup script (for deployment)
├── SMS_Spam_classifier.ipynb  # Training notebook
├── spam.csv               # Dataset
└── README.md              # Project documentation
