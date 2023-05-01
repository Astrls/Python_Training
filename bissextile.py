# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

try:
    annee = int(input("Saisissez une année : "))  # On attend que l'utilisateur saisisse l'année qu'il désire tester
    if annee <= 0:
        raise ValueError

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")


except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")