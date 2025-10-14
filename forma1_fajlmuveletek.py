
verseny_adatok = []

try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        for sor in fajl:
            verseny_adatok.append(sor)        

except IOError as ex:
    print(f"Fájl megnyitás hiba: {ex}")

#print(verseny_adatok)

    """
    1. [✔] Sorozatszámítás/összegzés
    2. [✔] Kiválasztás
    3. [✔] Megszámolás
    4. [✔] Eldöntés 1
       [✔] Eldöntés 2
    5. [✔] Maximum/minimum kiválasztás
    6. [✔] Keresés (lineáris)
    
    7. [] Kiválogatás (külön, helyben)
    8. [] Szétválogatás
    9. [] Unió
    10.[] Metszet
    
    11. Rendezés
       [] egyszerű cserés
       [] buborékos
       [] minimumkiválasztásos
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
    
#3. Hány versenyző teljesitett 300 pont felett?
db1=0
for i in range (1,len(verseny_adatok)):
    if (int(verseny_adatok[i].split(",")[1])>300):
        db1+=1
print(f"{db1} versenyző teljesített 300 pont felett")


#4.1 Van-e 0 pntos versenyző?
'''
ciklusvaltozo=1
while ciklusvaltozo<len(verseny_adatok) and int(verseny_adatok[ciklusvaltozo].split(",")[1])>0:
    ciklusvaltozo+=1
if ciklusvaltozo<len(verseny_adatok):
    print("Van 0 pontos versenyző")
else:
    print("Nincs 0 pontos versenyző")
'''


#4.2 Mindenki szerzett pontot a 2024-es szezon alatt?
ciklusvaltozo=1
while ciklusvaltozo<len(verseny_adatok) and int(verseny_adatok[ciklusvaltozo].split(",")[1])>0:
    ciklusvaltozo+=1
print(ciklusvaltozo)
if ciklusvaltozo>=len(verseny_adatok):
    print("MINDEKI SZERZETT PONTOT A 2024-ES SZEZON ALATT😎")
else:
    print("VAN OLYAN AKI NEM SZERZETT PONTOT A 2024-ES SZEZON ALATT😆")


# 5. Ki vezeti a tabellát? (Maximumkiválasztás)
max_ertek = int(verseny_adatok[1].split(",")[1])
max_index = 1
for i in range(2,len(verseny_adatok)):
    if (int(verseny_adatok[i].split(",")[1]))>max_ertek:
        max_index = i
        max_ertek = int(verseny_adatok[i].split(",")[1])
print(f"Ő vezet: {verseny_adatok[max_index].split(",")[0]}") 
       
#6. Kinek van 90 pontja?
i=1
while i<len(verseny_adatok) and int((verseny_adatok[i]).split(',')[1]) != 90:
    i+=1
    
if (i<len(verseny_adatok)):
    print(f"{(verseny_adatok[i]).split(',')[0]}-nek/nak van 90 pontja.")
else:
    print("Nincs olyan akinek 90 pontja van.")
 
 #7 Kik a Mercedes pilótái?
db2=0
merci=[]
for i in range(1, len(verseny_adatok)):
    if verseny_adatok[i].strip().split(",")[2]=="Mercedes":
        merci.append(verseny_adatok[i].split(",")[0])
        db2+=1
print(merci)
         
 

 
 
 
         