a = int(input("Ievadi skaitli a: "))

if a < 2:
    print("Nav pirmskaitlis")
else:
    pirmskaitlis = True
    i = 2

    while i * i <= a:
        if a % i == 0:
            pirmskaitlis = False
            break
        i += 1

    if pirmskaitlis:
        print("Ir pirmskaitlis")
    else:
        print("Nav pirmskaitlis")