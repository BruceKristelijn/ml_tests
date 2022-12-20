# Script will predict for ticker
from dotenv import load_dotenv

import pickle, os
import pandas as pd
import numpy as np

name = input("Model / ticker name: ")

data_path = os.getcwd() + "/workspace/dat/dat_" + name + ".csv"
model_path = os.getcwd() + "/workspace/saved/" + name + "/"

krr = pickle.load(open(model_path + 'kernelridge.dat', 'rb'))
reg = pickle.load(open(model_path + 'linearregression.dat', 'rb'))

df = pd.read_csv(data_path)
data = [df.iloc[-24:]['close']]

krr_prediction = krr.predict(data)[-1]
reg_prediction = reg.predict(data)[-1]

print("Last close", df.iloc[-2:-1]['close'])
print("KRR Prediction: ", krr_prediction)
print("REG Prediction: ", reg_prediction)

# Display plot
import plotly.graph_objects as go
import plotly.io as pio

from datetime import datetime, timedelta

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'],name = name + " candles")])

lastdate = df.iloc[-1]['date']
lastdate = datetime.strptime(lastdate, '%Y-%m-%d %H:%M:%S')


dates = [lastdate + timedelta(hours=x) for x in range(0, len(krr_prediction) + 1)]

#insert
lastclose = df.iloc[-1:]['close'].values[0]

krr_prediction = np.insert(krr_prediction, 0, lastclose)
reg_prediction = np.insert(reg_prediction, 0, lastclose)

fig.add_scatter(x=dates, y=krr_prediction, mode='lines', line=dict(color="#fc0362", width=5),name ="KernelRidge")
fig.add_scatter(x=dates, y=reg_prediction, mode='lines', line=dict(color="#39fc03", width=5, dash='dash'),name ="LinearRegression")

fig.add_scatter(x=[lastdate, dates[-1]], y=[lastclose, (reg_prediction[-1] + krr_prediction[-1]) / 2], mode='lines', line=dict(color="#FFCD02", width=2, dash='dash'),name ="Indicator")

fig.update_layout(template="plotly_dark")
fig.show()