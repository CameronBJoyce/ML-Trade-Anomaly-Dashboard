import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

class TradeDataAnomalyDetection:
    def __init__(self, trade_data):
        self.trade_data = trade_data
    
    def perform_anomaly_detection(self):
        # Data preprocessing
        scaled_data = self.preprocess_data()
        
        # Model training
        model = self.build_model()
        model.fit(scaled_data, scaled_data, epochs=50, batch_size=32, verbose=0)
        
        # Anomaly detection
        reconstructions = model.predict(scaled_data)
        mse = np.mean(np.power(scaled_data - reconstructions, 2), axis=1)
        threshold = np.mean(mse) + 3 * np.std(mse)
        anomalies = mse > threshold
        
        anomaly_df = pd.DataFrame({'Trade Data': self.trade_data.index, 'Reconstruction Error': mse, 'Anomaly': anomalies})
        
        return anomaly_df
    
    def preprocess_data(self):
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.trade_data.values)
        scaled_data = np.expand_dims(scaled_data, axis=-1)
        
        return scaled_data
    
    def build_model(self):
        model = Sequential()
        model.add(LSTM(16, activation='relu', input_shape=(self.trade_data.shape[1], 1), return_sequences=True))
        model.add(LSTM(8, activation='relu', return_sequences=False))
        model.add(Dense(self.trade_data.shape[1]))
        model.compile(optimizer='adam', loss='mean_squared_error')
        
        return model