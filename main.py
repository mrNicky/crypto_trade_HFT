import cryptocompare
import sys

value = str(sys.argv[1])
budget = 1000
commission = 0.1
#leverage = 10
#stop_loss = True

class Crypto:
    def __init__(self):
        self.budget = budget
        self.action = 0
        self.statut = "want_to_buy"
        self.indice_previous = 0
        self.indice = cryptocompare.get_price(value, curr='USD')[value]['USD']
        print(self.indice, "USD")
        #buy
        self.action = float(self.budget / self.indice)
        self.indice_previous = self.indice
        self.statut = "want_to_sell"

    def position(self):
        self.indice = cryptocompare.get_price(value, curr='USD')[value]['USD']

        if self.statut == "want_to_sell":
            print("target SELLING, more than this value : ", float(self.indice_previous * 1.0025), " --- crypto value NOW: ", self.indice)
            if float(self.indice_previous * 1.0025) < float(self.indice):# 0.25%
              self.budget = float(self.indice * self.action) * (1 - commission / 100)
              self.action = 0
              self.indice_previous = self.indice
              self.statut = "want_to_buy"
              print("SELING AT price : ", self.indice)
              print("BDUGET now : ", self.budget)
              with open(f"balance_{value}.txt", "a") as myfile:
                  myfile.write(str(self.budget) + "\n")

        if self.statut == "want_to_buy":
              print("target BUY below this value: ", float(self.indice_previous * 0.9975), " ---- crypto value NOW: ", self.indice)
              if float(self.indice  * 1.0025) < float(self.indice_previous):
                  self.action = float(self.budget / self.indice) * (1 - commission / 100)
                  self.budget = self.action * self.indice
                  self.indice_previous = self.indice
                  self.statut = "want_to_sell"
                  print("buying AT price : ", self.indice)
                  print("BDUGET now : ", self.budget)

def simulation():
    """ Run every seconde : 1.0 """
    import threading
    threading.Timer(1.0, simulation).start()
    first.position()

first = Crypto()
simulation()
