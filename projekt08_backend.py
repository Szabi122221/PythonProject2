from flask import Flask, jsonify
import random

app = Flask(__name__)
@app.route("/api/data")
def get_data():
    szam = random.randint(1, 100)
    return jsonify({"uzenet": f"{szam}"})
if __name__ == '__main__':
    app.run(port=5000)

app.run()