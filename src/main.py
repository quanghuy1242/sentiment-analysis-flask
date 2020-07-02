from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras import Model
from .predit_helper import predict_on_text

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
    return "Homepage!!!"


@app.route("/api/predict", methods=["POST"])
def predict():
    text = request.json["text"]
    probs = predict_on_text(text, model)
    return jsonify({
        "text": text,
        "probabilities": probs
    })
