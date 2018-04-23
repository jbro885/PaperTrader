from django.db import models
from django.urls import reverse
import json
from PaperTraderApp.Balance.Balance import Balance

from PaperTraderApp.StockHandler.Stock import Stock
#from PaperTraderApp.StockHandler.StockObserver import StockObserver
# Create your models here.
MAX_LENGTH_NAME = 60
MAX_LENGTH_SYMB = 6
MAX_DIGITS = 20


class StockModel(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_NAME, unique=True)
    symbol = models.CharField(max_length=MAX_LENGTH_SYMB, unique=True)
    opening = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    closing = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    high = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    low  = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=2)
    volume = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=0)
    
    def __str__(self):
        return "{0} ({1})".format(self.name, self.symbol)

    def get_absolute_url(self):
        return reverse("stock-list", kwargs={ 'pk' : self.pk }) # We'll need this when it comes to deleting stock object

class AdminStockModel(models.Model):
    symb = models.CharField(max_length=MAX_LENGTH_NAME)
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    def get_absolute_url(self):
        return reverse("admin")

class PortfolioModel(models.Model):
    user = models.CharField(max_length=256)
    stocks = models.CharField(max_length=99999999, default=json.dumps({}))
    balance = models.FloatField(default=0.0)
    balance_obj = Balance()

    def get_balance(self):
        return self.balance

    def set_stocks(self, stock_list):
        print(stock_list)
        self.stocks = json.dumps(stock_list)

    def get_stocks(self):
        return json.loads(self.stocks)

    def get_absolute_url(self):
        return reverse("portfolio", kwargs={'pk' : self.pk})

    def set_balance(self, balance):
        self.balance = balance

    def add_balance(self, amount):
        self.balance_obj.add(amount)
        self.balance += amount
        self.save()

    def buy(self, stockObj, quantity):
        '''
            this will handle the balance exceptions
        '''
        #print(float(stockObj.getPrice()) * quantity)
        self.set_balance(self.balance_obj.sub(float(stockObj.getPrice()) * quantity))

        current_stocks = self.get_stocks()
        current_stocks[stockObj.getSymbol()] = current_stocks[stockObj.getSymbol()] + 1 if stockObj.getSymbol() in current_stocks.keys() else 1
        self.set_stocks(current_stocks)
        self.save()

        '''
            store stock in dict as tuple of quantity and price ( price can be used for history/gain? )
        '''
        self.__stocks[stock.getSymbol()] = (quantity, stock.getPrice())
    

