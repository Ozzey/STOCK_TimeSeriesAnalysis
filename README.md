# Stocks_Price_Predictor_Module2
Second Module of my Stocks price predictor program.

## How To Use:
****************************************************
### 1.Installing the Libraries:
```bash
pip install fbprophet yfinance plotly
pip install streamlit -q
```
****************************************************
### 2.Run main.py cell
****************************************************
### 3.Download ngrok:
```bash
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

!unzip -qq ngrok-stable-linux-amd64.zip
```
****************************************************
### 4.Use the following command to start local server:

a) For Google Colab: 
```bash
get_ipython().system_raw('./ngrok http 8501 &')

! curl -s http://localhost:4040/api/tunnels | python3 -c \
    'import sys, json; print("Execute the next cell and the go to the following URL: " +json.load(sys.stdin)["tunnels"][0]["public_url"])'
```

b) On your local system:
```bash
ngrok http https://localhost:8443
```
****************************************************
### 5. Run the web app through streamlit:
```bash
!streamlit run main.py
```
****************************************************
*Interactive Graph:*
![Interactive Graph:](https://github.com/Ozzey/Stocks_Price_Predictor_Module2/blob/main/Assets/newplot.png)
*Graph's Components:*
![Graph's Components:](https://github.com/Ozzey/Stocks_Price_Predictor_Module2/blob/main/Assets/components.png)

> Live Version of the web app can be found [here](https://share.streamlit.io/ozzey/stocks_price_predictor_module2/main/main.py)
