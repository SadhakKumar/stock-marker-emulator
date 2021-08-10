from typing import ValuesView
import mysql.connector
import requests


mydb = mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="natu@123",
  database="stocks"
  )  

mycursor = mydb.cursor()


name = input("enter your name:")


print("list of companies:-\napple : AAPL\nmicrosoft : MSFT\ntesla : TSLA\ngoogle : GOOGL\nVisa  :V\nJPMorgan Chase : JPM\nIntel : INTC\nNike : NKE\nCoca-Cola : KO\nMcDonald’s : MCD\nWalmart : WMT\nDisney : DIS")

value = input("enter the companies name you want:")
url = "https://api.polygon.io/v2/aggs/ticker/" + value + "/prev"

parameters = {"stocksTicker":"AAPL", "unadjusted":"true","apiKey":"uGhLlxMaf0wperszH6IXuApesZNNzCh5"}

response = requests.get(url,params=parameters)

response_json = response.json()

x= response_json['results'][0]['c']


def buy():
  print("the cost of the stock is :",x)
  number_of_stocks = int(input("enter the number of stocks you want:"))
  cost_to_stock = number_of_stocks*x
  mycursor.execute("select "+value+" from stonks where FirstName ='%s'"%(name))
  myresult = mycursor.fetchall()
  print("you bought",number_of_stocks,"stocks")
  
  for row in myresult:
    
    myresult = row[0]
  mycursor.execute("UPDATE stonks SET money = money-'%f' WHERE FirstName ='%s'"%(cost_to_stock,name,))
  mycursor.execute("UPDATE stonks SET "+value+"='%f'+'%f' WHERE FirstName = '%s'"%(myresult,number_of_stocks,name,))
  
  mydb.commit()

def sell():
  print("the cost of the stock is :",x)
  mycursor.execute("select "+value+" from stonks where FirstName ='%s'"%(name))
  myresult = mycursor.fetchall()
  
  for row in myresult:
    print("you have",row[0],"stocks")
    myresult = row[0]

  sell_stocks = int(input("how much you want to sell:"))
  left_stocks = myresult-sell_stocks
  amount_after_selling = sell_stocks*x
  mycursor.execute("UPDATE stonks SET money = money +'%f' WHERE FirstName = '%s'"%(amount_after_selling,name,))
  mycursor.execute("UPDATE stonks SET "+value+"='%f' WHERE FirstName ='%s'"%(left_stocks,name,))
  mydb.commit()
  print("you sold",sell_stocks,"stocks")


def check_stock_price():
  print("the price of the stock you selected is:",x)


def money():
  mycursor.execute("select money FROM stonks WHERE FirstName = '%s'"%(name))
  myresult = mycursor.fetchall()
  print(myresult)


what_will_you_do = input("kya kerna hai?")
if what_will_you_do == 'buy':
  buy()
if what_will_you_do == 'sell':
  sell()
if what_will_you_do == 'price'or'check price'or'check stock price':
  check_stock_price()
if what_will_you_do == 'money':
  money()














