from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/data')
def data():
    return jsonify({
        'timestamp': int(time.time() * 1000),  # milliseconds
        'value': random.randint(1, 100)
    })

if __name__ == '__main__':
    app.run(debug=True)
