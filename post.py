from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
   return jsonify(request.json)
