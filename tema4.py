# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

for element in progres:
    print(element, end="")
while incercari_ramase > 0 and "_" in progres:
    litera=input("Introdu o litera:")
    if len(litera) !=1 or litera in litere_incercate:
        print("Litera este invalida,introdu o litera valida")
        continue
        if litera in litere_incercate:
            print("Ai incercat aceasta litera")
    litere_incercate.append(litera)
    i=0
    if litera in cuvant_de_ghicit:
        print(f"Ai ghicit litera {litera}")
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i]==litera:
                progres[i]=litera
        print(progres)
    else:
        incercari_ramase = incercari_ramase - 1
        print(f"Mai incearca,mai ai {incercari_ramase} incercari ")
if incercari_ramase == 0:
    print(f'Ai pierdut,cuvantuld era {cuvant_de_ghicit} ')
else:
    print(f"FELICITARI:)) AI GHICIT CUVANTUL {cuvant_de_ghicit}")





