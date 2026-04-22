# 📧 Spam Detector Web App

A machine learning web app that detects whether an email is **Spam** or **Ham (Not Spam)**.

## 🚀 Live Demo
> Paste any email text and instantly find out if it's spam!

## 🛠️ Built With
- **Python** - Backend logic
- **Flask** - Web framework
- **Scikit-learn** - Machine Learning model
- **SQLite** - Database to store prediction history
- **HTML & CSS** - Frontend design

## ⚙️ How to Run Locally

1. Clone the repo
   git clone https://github.com/Dilanka0410/spam-detectorr.git

2. Install dependencies
   pip install flask scikit-learn

3. Run the app
   python app.py

4. Open in browser
   http://127.0.0.1:5000

## 📁 Project Structure
spam-detector/
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── Untitled.ipynb
└── templates/
    └── index.html

## 📊 How It Works
1. User pastes an email into the text box
2. The trained ML model analyzes the text
3. Result is shown as ✅ Ham or 🚨 Spam
4. Every prediction is saved to the database

## 👨‍💻 Author
**Dilanka**
GitHub: [@Dilanka0410](https://github.com/Dilanka0410)
