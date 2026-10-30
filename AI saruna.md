Izveido programmu kura ievada skaitli a (a vesels, pozitivs (>= 0) skaitļis).
Programmai jāparbauda vai tas ir pirmskaitlis (a dalas tikai uz a un 1). 
Var parbaudit dalitajus līdz sakne no a (dalitajs kvadrata <= a).

ChatGPT said:
Šeit ir programma Python valodā, kas ievada veselu nenegatīvu skaitli a un pārbauda, vai tas ir pirmskaitlis.


python
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
Kā programma darbojas?
Ievada skaitli a.

Ja a ir mazāks par 2, tas nav pirmskaitlis.

Pārbauda dalītājus, sākot no 2, līdz i * i <= a.

Ja atlikums a % i == 0, skaitlis dalās bez atlikuma un nav pirmskaitlis.

Ja neviens dalītājs netiek atrasts, skaitlis ir pirmskaitlis.

Piemērs:

Ievade: 7 → Ir pirmskaitlis

Ievade: 9 → Nav pirmskaitlis

Ievade: 2 → Ir pirmskaitlis


You said:
Izveido programmu kura lietotajs ievada veselos skaitļus.
Programmai jāizvada pēc katra ievadita skaitļa ievaddatu statistiku:
    maksimalais, minimalais, ievadito skaitļu sdaudzums, videjas aritmetiskais. 
Jābūt opcijaj lai lietotajs varētu pabeigt darbību ar programmu (Piemēram jautajums: Vēlēties turpināt? YES/NO)

ChatGPT said:
Šeit ir programma Python valodā, kurā lietotājs ievada veselus skaitļus. Pēc katra ievadītā skaitļa programma izvada statistiku: maksimālo, minimālo, ievadīto skaitļu skaitu un vidējo aritmētisko.


python
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
Kā programma darbojas?
Izveido sarakstu skaitli, kurā glabā ievadītos skaitļus.

Ar while True nodrošina atkārtotu skaitļu ievadi.

Katru ievadīto skaitli pievieno sarakstam ar append().

Izmanto:

max() – lielākā skaitļa atrašanai.

min() – mazākā skaitļa atrašanai.

len() – ievadīto skaitļu skaita noteikšanai.

sum() / len() – vidējā aritmētiskā aprēķināšanai.

Pēc statistikas parādīšanas lietotājs izvēlas, vai turpināt.

Ja ievada NO, programma beidz darbu ar break.

Piemērs:


text
Ievadi veselu skaitli: 5
Maksimālais skaitlis: 5
Minimālais skaitlis: 5
Ievadīto skaitļu skaits: 1
Vidējais aritmētiskais: 5.0
Vai vēlies turpināt? (YES/NO): YES

Ievadi veselu skaitli: 10
Maksimālais skaitlis: 10
Minimālais skaitlis: 5
Ievadīto skaitļu skaits: 2
Vidējais aritmētiskais: 7.5
Vai vēlies turpināt? (YES/NO): NO

Programma beidz darbu!

You said:
skaitli.append(a), .upper() kas tas ir?

ChatGPT said:
Tie ir Python valodas elementi, kas palīdz darboties ar sarakstiem un tekstu.

1. skaitli.append(a)
append() nozīmē pievienot elementu saraksta beigās.

Piemēram:


python
skaitli = []

a = 5
skaitli.append(a)

a = 10
skaitli.append(a)

print(skaitli)
Rezultāts:


text
[5, 10]
Tātad katrs ievadītais skaitlis tiek saglabāts sarakstā skaitli.

2. .upper()
upper() pārveido visus teksta burtus par lielajiem burtiem.

Piemērs:


python
atbilde = input("Vai vēlies turpināt? ")
atbilde = atbilde.upper()

print(atbilde)
Ja lietotājs ievada yes, programma pārveido to par YES.

Tas ir noderīgi, jo lietotājs var rakstīt:

yes

Yes

YES

Visos gadījumos programma saņems YES.

Īsumā
append() – pievieno skaitli sarakstam.

upper() – pārveido tekstu par lielajiem burtiem.

Abi ir Python iebūvēto datu tipu metožu piemēri.


