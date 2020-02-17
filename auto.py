import time, os, sys, pickle

save_file = "savegame.dat"

with open(save_file, "rb") as f:
    verlevel, number, coins, agilidade, gain, gain2, gain3, gain4, countmine, double, price1, price2, price3, expcount, exp, level = pickle.load(f)
while (True):
    coins += 1
    time.sleep(1)
    with open('savegame.dat', 'wb') as f:
        pickle.dump([verlevel, number, coins, agilidade, gain, gain2, gain3, gain4, countmine, double, price1, price2, price3, expcount, exp, level], f, protocol=2)