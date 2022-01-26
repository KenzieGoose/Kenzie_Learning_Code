import decimal

def drange(x, y, jump):
  while x < y:
    yield float(x)

list(drange(0, 100, '0.1'))[-1]