import pickle

verlevel = 3
number = 0
coins = 0
agilidade = 10
gain = 1
gain2 = 1
gain3 = 1
gain4 = 1
countmine = 3
double = False
price1 = 10
price2 = 10
price3 = 25
expcount = 25
exp = 0
level = 0

with open('savegame.dat', 'wb') as f:
    pickle.dump([verlevel, number, coins, agilidade, gain, gain2, gain3, gain4, countmine, double, price1, price2, price3, expcount, exp, level], f, protocol=2)