skaitli = []

while True:
    a = int(input("Ievadi veselu skaitli: "))
    skaitli.append(a)

    print("Maksimālais skaitlis:", max(skaitli))
    print("Minimālais skaitlis:", min(skaitli))
    print("Ievadīto skaitļu skaits:", len(skaitli))
    print("Vidējais aritmētiskais:", sum(skaitli) / len(skaitli))

    atbilde = input("Vai vēlies turpināt? (YES/NO): ").upper()

    if atbilde == "NO":
        print("Programma beidz darbu!")
        break
