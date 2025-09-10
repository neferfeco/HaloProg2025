import random


# Lista létrehozása
szamok = []

# Lista feltöltése 100 db random kétjegyű egész számmal
for i in range(100):
    szam = random.randint(10, 99)
    szamok.append(szam)

# Ellenőrzés
print(szamok)


# EGYSZÁM JÁTÉK
jatek_szam = 0
nem_talaldDB = 0

kitalalando_szam = szamok[random.randint(len(szamok))]

tipp = int(input("Tipped? (egész szám): "))

while(tipp != kitalalando_szam):
    tipp = int(input("Tipped? (egész szám): "))

print("Kitaláltad a kitalálandó számot!")

folytatas = input("Akarsz-e még játszani? [I/N]")

if(folytatas == "I"):
    # ??????????
    aa=1
else:
    exit()


