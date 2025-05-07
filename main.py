import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

def fetch_data(ticker):
    df = yf.download(ticker, period="2y")
    return df['Close'].values.reshape(-1, 1)

def preprocess(data):
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)
    x, y = [], []
    for i in range(60, len(data_scaled)):
        x.append(data_scaled[i-60:i])
        y.append(data_scaled[i])
    return np.array(x), np.array(y), scaler

def build_model():
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(60, 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def predict_stock(ticker):
    data = fetch_data(ticker)
    x, y, scaler = preprocess(data)
    model = build_model()
    model.fit(x, y, epochs=5, batch_size=32, verbose=0)
    last_60 = data[-60:].reshape(-1, 1)
    last_60_scaled = scaler.transform(last_60)
    x_test = np.expand_dims(last_60_scaled, axis=0)
    prediction = model.predict(x_test)
    return float(scaler.inverse_transform(prediction)[0][0])
  
