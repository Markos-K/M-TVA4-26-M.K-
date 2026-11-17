print("Tere maailm")
print("Tere veel kord")
print("Mul on", 3, "kassi")
print("Aasta on", 2026, sep="-")

print("2026", "10", "01", sep="-")
print("Sama ", end="") # end="\n" Enter, "\t" =Tab
print("rida")
#1,3 Muutujad ja omistamine
nimi="Python" #str-sõne
vanus=25 #int-täisarv
laius=0.75 #float
täna_on_koolis=True #bool-tõeväärtus

print(nimi*3)
print(nimi+nimi)
print(vanus+laius)
print(täna_on_koolis)

KÄIBEMAKS = 0.24
hind = 100 
print(hind*(1+KÄIBEMAKS))
nimi=input("mis on sinu nimi")
print(f"Tere,{nimi}")
#a ja b on tekstid
a = int (input("Esimene arv: "))
b = int (input("Teine arv: "))
print(a + b)

#Aritmeetilised põhioperatsioonid
print(f"astendamine{a}**{b} ={a**b}")
print(f"korrutamine{a}*{b} ={a*b}")
print(f"jagamine{a}/{b} ={a/b}")
print(f"jagamise täisarvuline osa{a}//{b} ={a//b}")
print(f"jagamisjääk{a}%{b} ={a%b}")
print(f"liitmine{a}+{b} ={a+b}")
print(f"lahutamine{a}-{b} ={a-b}")

#1.7 pythoni moodulid
from time import *
from os import *
print("valgusfoor käivitu")
print #tühi rida
system("cls")
print("punane põleb ja kollane põlevad - valmistu!")
sleep(2)
system("cls")
print("kollane põleb - sõida!")
sleep(5)
system("cls")
print("kollane põleb - tähelepane!")
sleep(2)
system("cls")
print("valgusfoorlõpetas töö.")
