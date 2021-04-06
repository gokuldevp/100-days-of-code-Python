import requests

URL = "https://opentdb.com/api.php?amount=10&type=boolean"
PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

with requests.get(url=URL, params=PARAMETERS) as question_bank:
    question_bank.raise_for_status()
    question_json = question_bank.json()
    question_data = question_json["results"]
