import requests
import sqlite3
import time
from datetime import datetime
from datetime import datetime
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
def curr():
   cont=requests.get('https://www.google.com/finance/quote/USD-KES')
   dat=bs(cont.content,'html.parser')
   bit=dat.find_all('div',{'class':'YMlKec fxKbKc'})[0].text
   return float(bit)
