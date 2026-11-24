
from flask import Flask, jsonify, render_template
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "application": "Payment API"
    })


@app.route('/payments')
def payments():
    return jsonify({
        "payment_id": 1001,
        "customer": "John",
        "amount": 5000,
        "currency": "INR",
        "status": "SUCCESS"
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

