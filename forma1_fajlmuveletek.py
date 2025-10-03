
verseny_adatok = []

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        for sor in fajl:
            verseny_adatok.append(sor)        

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

#print(verseny_adatok)

    """
    1. Sorozatszámítás/összegzés
    2. Kiválasztás
    3. Megszámolás
    4. Eldöntés 1
        Eldöntés 2
    5. Maximum/minimum kiválasztás
    6. Keresés (lineáris)
    
    7. Kiválogatás (külön, helyben)
    8. Szétválogatás
    9. Unió
    10. Metszet
    
    11. Rendezés
        eygszerű cserés
        buborékos
        minimumkiválasztásos
    """


# 1. Mennyi a pontszám átlag?
pontszam = 0 
db = len(verseny_adatok)-1
for i in range(1,len(verseny_adatok)):
    sor=verseny_adatok[i].split(",")
    pontszam=pontszam+int(sor[1])
atlag=pontszam/db
print(f"Pontszámok átlaga: {atlag}")






#2. Mi a bekért versenyzo adatai?
pilota=input("Kérek egy pilótát:")
ciklusvaltozo=1
while verseny_adatok[ciklusvaltozo].split(",")[0]!=pilota:
    ciklusvaltozo+=1
print(verseny_adatok[ciklusvaltozo])
    
    








