import re
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras import Model
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .predit_helper import predict_on_text

# Use the application default credentials
cred = credentials.Certificate('assets/account-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'reviews')

app = Flask(__name__)

init_model = load_model("assets/model.h5")
model = Model(
    inputs=init_model.input,
    outputs=[
        init_model.output,
        init_model.get_layer('attention_weight').output
    ]
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/predict", methods=["POST"])
def predict():
    print(request.json)
    text = request.json["text"]
    probs = predict_on_text(text, model)
    doc_ref.document(re.sub("[:|/.]", "-", datetime.now().isoformat())).set({
        'text': request.json['text'],
        'probs': probs
    })
    return jsonify({
        "text": text,
        "probabilities": probs
    })
