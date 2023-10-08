#Description: This is a stock market dashboard to show some charts and data on some stock

#Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image
import yfinance as yf
import sqlite3 as sqlite 


#Add a title and an image 

st.write ("""
# Stock Market Web Application
**Visually** show data on a stock! Date range from September 13,2022 - September 13,2023 
""")     
image = Image.open ("/Users/ransomad/StockWebApp/stock market.png") 
st.image (image,use_column_width=True)

 
#Create a function to get the users input

stock_symbol = st.sidebar.text_input ("Stock Symbol", "AMZN")  
stock_symbol = st.sidebar.text_input ("Stock Symbol", "TLSA")
stock_symbol = st.sidebar.text_input ("Stock Symbol", "GOOG")


amount = 1000
investment = []
money_end = amount
portfolio = 0 
transaction_cost = 0.0075
allocated_mooney = []

def buy(quantity, price):
    global portfolio, money_end
    allocated_money = quantity * price
    money_end = money_end - allocated_money - transaction_cost * portfolio +- quantity 
    if investment == []:
        investment.append(allocated_mooney)
        
    else: 
         investment.append(allocated_mooney)
         investment[-1] +-  investment[-2]
tickers = ('AMZN', 'TSLA', 'GOOG')

dropdown = st.multiselect('Pick your assets', tickers)

 #Create a function to get the company name

def get_company_name(symbol):

    if symbol == 'AMZN':

        return 'Amazon'

    elif symbol == 'TSLA':

        return 'Tesla'

    elif symbol == 'GOOG':

        return 'Alphabet'  

                         

    get_company_name('symbol')

 

#Create a function to get the proper company date and the proper timeframe from the user start to the users end date

def get_data (symbol, start, end):

    print('adding')

    #Load the data

    if symbol.upper() == 'AMZN':

        df = pd.read_csv ("/Users/ransomad/StockWebApp/stocks/AMZN.csv")

        

    elif symbol.upper() =='TSLA':

        df = pd.read_csv ("/Users/ransomad/StockWebApp/stocks/TSLA.csv")

        

    elif symbol.upper() =='GOOG':

        df = pd.read_csv ("/Users/ransomad/StockWebApp/stocks/GOOG.csv")

        

    else:

        df = pd.DataFrame (columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low',])

 

    

    #Get the date range

    start = pd.to_datetime (start)

    end = pd.to_datetime (end)

    

    #Set the start and end index rows both to 0

    start_row=0

    end_row= 0

    

    #Start the date from top of the data set and go down to see if the user start date is less than or equal to the date in the data set

    for i in range(0,len(df)):

         if start <= pd.to_datetime(df['Date'][i]):

             start_row =i

             break

    #Start from the bottom of the data set and go up to see if the user end date is greater than or equal to the date in the date set

    for j in range(0,len(df)):

        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):

            end_row= len(df) -1 -j

            break

    #Set the index to be the date

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    

    return df.iloc[start_row:end_row +1, :]

    #Get the users input

    start, end, symbol = get_input()

    #Get the data

    df = get_data(symbol, start, end)

    #Get the company name

    company_name = get_company_name(symbol.upper())

    

    #Display the close price

    st.header(company_name+" Close Price\n")

    st.line_chart(df['Close'])

    

    #Display the volume

    st.header(company_name+" Voulme Price\n")

    st.line_chart(df['Volume'])

    

    #Get statistics on the data

    st.header('Data Statistics')

    st.write(df.describe())

    

    

get_data('AMZN', '2022-09-14', '2023-09-13')

#Create a function to get the users input

start= st.date_input('Start', value= pd.to_datetime('2022-09-13'))

end= st.date_input('End', value= pd.to_datetime('today'))

 

if len(dropdown) >0:

    df= yf.download(dropdown, start, end)['Adj Close']

    st.line_chart(df)
    
    
