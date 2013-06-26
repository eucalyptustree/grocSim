"""
Grocery store checkout line simulation.
"""

import random

class shopper:
    def __init__(self):
        self.cart = random.randint(1,24)
        self.waitTime = 0
        self.inLine = True
    def tick(self):
        self.waitTime +=1
    def checkout(self):
      pass



class checkoutLine:
    def __init__(self):
        pass


print 'hello world'
