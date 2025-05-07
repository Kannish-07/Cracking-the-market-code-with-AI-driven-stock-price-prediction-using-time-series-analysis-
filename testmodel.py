from main import predict_stock

def test_prediction():
    result = predict_stock("AAPL")
    print(f"Predicted Price for AAPL: ${result:.2f}")
    assert result > 0, "Prediction should be a positive number."

if __name__ == '__main__':
    test_prediction()
  
