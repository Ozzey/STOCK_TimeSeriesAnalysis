#Predicting Stocks Prices through FbProphet ML module
#Importing Librarues
import streamlit as st
import yfinance as yf

from datetime import date
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

#Start & End date  of data
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

#Creating a gui using Streamlit
st.title("STOCKS PREDICTION")

#Drop-down for selection of stocks to predict
stocks = ('TSLA', 'AMZN','AAPL','YNDX','BTC-USD')
selected_stock = st.selectbox('Select Your Preferred Stocks for Prediction', stocks)

n_years = 1
period = n_years*365

#cache for loading data
@st.cache
def load_data(ticker):
  data = yf.download(ticker, START, TODAY)
  data.reset_index(inplace = True)
  return data

data_load_state = st.text("Loading Data...")
data = load_data(selected_stock)
data_load_state.text("Loading Data...")

#Prediction of prices using Prophet
df_train = data[['Date','Close']]
df_train = df_train.rename(columns = {"Date":"ds", "Close":'y'})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods = period)

forecast = m.predict(future)

st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m,forecast)
st.plotly_chart(fig1)

#Extra Components graphs
st.write("COMPONENTS")
fig2 = m.plot_components(forecast)
st.write(fig2)
