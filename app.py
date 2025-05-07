from flask import Flask, request, jsonify
from main import predict_stock

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI Stock Price Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        ticker = data.get('ticker', 'AAPL')  # Default to AAPL if not provided
        prediction = predict_stock(ticker)
        return jsonify({
            'ticker': ticker,
            'predicted_price': round(prediction, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
  
