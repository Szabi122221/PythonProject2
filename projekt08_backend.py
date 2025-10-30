from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/api/data")
def get_data():
    return jsonify({"uzenet": "Udv a backendbol"})
if __name__ == '__main__':
    app.run(port=5000)

app.run()