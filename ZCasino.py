import math
import random

argent = 1000
continuer_partie = true
print("Bienvenue au casino, vous avez ", argent, "$")

while continuer_partie:
    nbpari = -1
    while nbpari < 0 or nbpari > 49:
        try:
            nbpari = int(input("Choisissez votre numéro: "))
            nbwin = int(random.randrange(49))
            mise = int(input("Choisissez le montant à miser"))

