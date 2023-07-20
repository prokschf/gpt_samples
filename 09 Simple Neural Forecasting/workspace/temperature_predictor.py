import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

class TemperaturePredictor:
    def __init__(self, sequence):
        self.sequence = sequence
        self.model = Sequential()

    def prepare_data(self):
        X, y = [], []
        for i in range(len(self.sequence)-3):
            X.append(self.sequence[i:i+3])
            y.append(self.sequence[i+3])
        return np.array(X), np.array(y)

    def train(self):
        X, y = self.prepare_data()
        X = X.reshape((X.shape[0], X.shape[1], 1))
        self.model.add(LSTM(50, activation='relu', input_shape=(3, 1)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')
        self.model.fit(X, y, epochs=200, verbose=0)

    def predict(self):
        predictions = []
        input_seq = np.array(self.sequence[-3:])  # Convert to numpy array here
        for _ in range(20):
            input_seq = input_seq.reshape((1, len(input_seq), 1))
            prediction = self.model.predict(input_seq, verbose=0)
            predictions.append(prediction[0][0])
            input_seq = np.append(input_seq[0][1:], prediction)
        return predictions

