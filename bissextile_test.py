while annee <= 0:

    try:
        annee = int(input("Entrez une année: "))
        assert annee > 0

    except ValueError:
        input("veuillez entrer un nombre: ")
    except AssertionError:
        input("Veuillez entrer une année > 0: ")

        if annee % 4 == 0:
            if annee % 400 == 0 or annee % 100 != 0:
                print("C’est une année bissextile")
            else:
                print("Ce n’est pas une année bisextile")
        else:
            print("Ce n’est pas une année bisextile")