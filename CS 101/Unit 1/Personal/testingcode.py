#shop
bal = 100

sword = 10
sword2 = 20
bow = 20
armor = 50
potion = 5
big_potion = 10

while True:
    choice = input("what do you want to buy?")
    if choice == "sword":
        bal -= sword
        print("You have bought a sword")
        print(bal)
    elif choice == "sword2":
        bal -= sword2
        print("You have upgraded your sword")
        print(bal)
    elif choice == "bow":
        bal -= bow
        print("You have bought a bow")
        print(bal)
    elif choice == "armor":
        bal -= armor
        print("You have bought armor")
        print(bal)
    elif choice == "potion":
        bal -= potion
        print("You have bought a potion")
        print(bal)
    elif  choice == "big_potion":
        bal -= big_potion
        print("You have bought a big_potion")
        print(bal)
    else:
        print("can you repeat that")
    if bal < 0:
        pass
        print("you dont have enough money")
    z = input("anything else")
    if z == "no":
        break
    else:
        pass