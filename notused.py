from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/vandyck/<int:user_id>/<string:name>")
def index(user_id, name):
    return jsonify({
        'message': 'Hello',
        "user_id": user_id,
        "name": name
    }), 200

@app.route('/vandyck', methods=['POST'])
def vandyck():
    return 'Vandyck'

if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )