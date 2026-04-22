from flask import Flask, request, render_template
import pickle

# Flask app create
app = Flask(__name__)

# Load trained model
model = pickle.load(open("spam_model.pkl", "rb"))

# ✅ FIX 1: Load vectorizer (was missing — caused NameError on every prediction)
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email"]   # or message

    # convert text -> vector
    data = vectorizer.transform([email])

    prediction = model.predict(data)[0]

    # ✅ FIX 2: Pass 'prediction_text' to match what index.html expects
    # Also convert raw model output (0/1) to a human-readable label
    prediction_text = "🚨 Spam Email!" if prediction == 1 else "✅ Not Spam (Ham)"

    return render_template("index.html", prediction_text=prediction_text, user_message=email)

# Run app
if __name__ == "__main__":
    app.run(debug=True)
