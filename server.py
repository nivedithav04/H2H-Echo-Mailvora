from flask import Flask, request, jsonify
from mail_agent import process_email

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    email = request.json
    result = process_email(email)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
