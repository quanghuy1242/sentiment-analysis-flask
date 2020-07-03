# Flask Server for running pridiction model

## Prerequisites
- Ubuntu 18.04 or later (or Windows 10 WSL)
- Python 3.7

## Install

```bash
python3.7 -m venv venv-3.7 # Create virtual environment
source venv-3.7/bin/activate # active venv
pip install -r requirements.txt # install module from requirements.txt
python -m flask run # run flask development server
```

## Setup the firestore database
You must setup firestore database!!!

## Usage
### With UI
Open address on your bash screen for accessing homepage

### API
The only way to predict a text is sent a POST request to `/api/predict` with body `{ "text": string }`

Example using curl:
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ "text": "Sản phẩm tốt!" }' \
  http://localhost:5000/api/predict
```