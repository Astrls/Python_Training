try:
    resultat = numerateur / denominateur
except NameError:
    print("la variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("le résultat obtenu est", resultat)

finally:
    pass

var = 5
assert var == 5
assert var == 8