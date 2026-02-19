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
├── app.py                     # Streamlit app
├── model.pkl                  # Trained ML model
├── vectorizer.pkl             # TF-IDF vectorizer
├── requirements.txt           # Python dependencies
├── Procfile                   # For deployment
├── setup.sh                   # Setup script (for deployment)
├── SMS_Spam_classifier.ipynb  # Training notebook
├── spam.csv                   # Dataset
└── README.md                  # Project documentation
```

---

## ⚙️ Installation & Running Locally

**1️⃣ Clone the repository**
```bash
git clone https://github.com/Sarvagya45/SMS-Spam-Classifier.git
cd SMS-Spam-Classifier
```

**2️⃣ Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Linux/Mac
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Download NLTK resources**  
Run Python and execute:
```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

**5️⃣ Run the app**
```bash
streamlit run app.py
```
The app will open in your browser 🚀

---

## 🧪 Example Inputs

**Spam Examples:**
- "Congratulations! You have won ₹10,00,000. Click the link now to claim your prize."
- "Free entry in a lucky draw! Text WIN to 54321 and get a chance to win cash."

**Not Spam Examples:**
- "Hey, are we meeting tomorrow at 10 am?"
- "Please send me the notes from yesterday's class."

---

## 📊 Model Details

| Property | Details |
|---|---|
| Feature Extraction | TF-IDF Vectorizer |
| Algorithm | Multinomial Naive Bayes |
| Trained on | SMS Spam Dataset |
| Output | `1` → Spam, `0` → Not Spam (Ham) |

---

## ⚠️ Known Limitations

- The model may sometimes misclassify messages with new or uncommon wording
- This is a demo / educational project, not production-grade spam filtering
- Free hosting may cause cold start delays

---

## 📌 Future Improvements

- Add probability/confidence score
- Improve preprocessing and feature engineering
- Try advanced models (Logistic Regression, SVM, etc.)
- Add message history & analytics
- Improve UI/UX

---

## 👨‍💻 Author

**Sarvagya Gupta**  
GitHub: https://github.com/Sarvagya45

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it really helps and motivates me to build more cool stuff 😄
