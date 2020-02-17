import time, os, sys, pickle

os.system('pythonw "auto.py"')

save_file = "savegame.dat"

with open(save_file, "rb") as f:
    verlevel, number, coins, agilidade, gain, gain2, gain3, gain4, countmine, double, price1, price2, price3, expcount, exp, level = pickle.load(f)

while True:
    os.system("cls")
    print("                  Mine Game")
    print("---------------------------------------------------")
    print("PARA SALVAR O JOGO VOCÊ DEVE SAIR UTILIZANDO A OPÇÃO '0'")
    print("---------------------------------------------------")
    if exp == expcount:
        level += 1
        expcount += 25
        exp = 0
    if agilidade == 1:
        print("O tempo de mineraçâo é de", agilidade, "Segundo")
    else:
        print("O tempo de mineração é de", agilidade, "Segundos")
    print("---------------------------------------------------")
    if gain2 == 1:
        print("A quantidade de coins por mineração é de", gain2, "Coin (por minerador)")
    else:
        print("A quantidade de coins por mineração é de", gain2, "Coins (por minerador)")
    print("---------------------------------------------------")
    print('')
    print('')
    print("Você é level:", level,)
    print("")
    if coins == 1:
        print("Voce tem", int(coins), "Coin")
    else:
        print("Voce tem", int(coins), "Coins")
    print("")
    print("Opções:")
    print("1: Minerar")
    print("2: Loja")
    print("0: Salvar e Sair")
    print("#: Resetar Jogo")
    print("")
    run = input("O que você deseja: ")
    sec = 0
    number = 0
    if run == "1":
        while sec < agilidade:
            print(">>>>>>", sec + 1, "<<<<<<")
            time.sleep(1)
            sec += 1
            number += 1
            if number == agilidade:
                coins += gain
                exp += 1
    elif run == "2":
        os.system("cls")
        print("Produtos:")
        print("")
        if agilidade == 1:
            print("1: Diminuir velocidade de mineração (1 segundo): Level Max.")
        else:
            print("1: Diminuir velocidade de mineração (1 segundo):", price1, "Coins")
        print("")
        print("2: Aumentar coins por mineração (1 coin):", price2, "Coins")
        print("")
        if level < 3:
            print("3: Minerador Duplo (level 3)")
        elif double == False:
            print("3: Minerador Duplo:", price3, "Coins")
        elif countmine == 4:
            print("3: Minerador Duplo: Level Max.")
        else:
            print("3: Minerador x", countmine, ":", price3, "Coins")
        print("")
        oploja = input("Qual produto deseja?: ")
        if oploja == "1":
            if agilidade != 1:
                if coins < price1:
                    print("")
                    print("Coins Insuficientes")
                    time.sleep(2)
                else:
                    agilidade -= 1
                    coins -= price1
                    price1 += 15
                    print("")
                    print("Compra Efetuada. Velocidade de mineração:", agilidade, "Segundos")
                    print("")
                    time.sleep(3)
            else:
                print("Upgrade se encontra no maximo")
                time.sleep(3)
        elif oploja == "2":
            if coins < price2:
                print("")
                print("Coins Insuficientes")
                time.sleep(2)
            else:
                if double == True:
                    gain3 += 1
                    gain = gain4 * gain3
                else:
                    gain3 += 1
                    gain += 1
                coins -= price2
                price2 += 15
                gain2 += 1
                print("")
                print("Compra Efetuada. Coins por mineração:", gain2, "Coins")
                print("")
                time.sleep(3)
        elif oploja == "3":
            if level < verlevel:
                print("Voce precisa ser level",verlevel,"para comprar isso.")
                print("")
                time.sleep(3)
            elif countmine == 4:
                print("Upgrade está no máximo.")
                time.sleep(2)
            else:
                if coins < price3:
                    print("")
                    print("Coins Insuficientes")
                    print("")
                    time.sleep(2)
                else:
                    if double == False:
                        double = True
                        print("Compra Efetuada. Minerador Duplo ativado.")
                    else:
                        print("Compra Efetuada. Minerador x", countmine)
                        countmine += 1
                    coins -= price3
                    price3 += 50
                    gain4 +=1
                    gain = gain4 * gain3
                    time.sleep(3)
                    verlevel = 5
    elif run == "0":
        with open("savegame.dat", "wb") as f:
            pickle.dump([verlevel, number, coins, agilidade, gain, gain2, gain3, gain4, countmine, double, price1, price2, price3, expcount, exp, level], f)
            break
    elif run == "#":
        os.system("cls")
        print("Tem Certexa que deseja resetar o jogo? (VOCÊ PERDERÁ TODO O PROGRESSO!)")
        print("")
        pq = input("(Escreva 'sim' para resetar, enter ou qualquer outra coisa para cancelar): ")
        if pq == "sim":
            verlevel = 3
            number = 0
            coins = 0
            agilidade = 10
            gain = 1
            gain2 = 1
            gain3 = 1
            gain4 = 1
            countmine = 0
            double = False
            price1 = 10
            price2 = 10
            price3 = 25
            expcount = 25
            exp = 0
            level = 0

            with open("savegame.dat", "wb") as f:
                pickle.dump([verlevel, number, coins, agilidade, gain, gain2, gain3, gain4, countmine, double, price1, price2, price3, expcount, exp, level], f)
            os.system("cls")
            print("Jogo Resetado!")
            time.sleep(3)
    else:
        print("Opção inválida")
        print("")
        time.sleep(2)
        continue
