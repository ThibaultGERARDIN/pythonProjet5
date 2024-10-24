# Écrivez votre code ici !


def square(number):
    if (type(number) is float) or (type(number) is int):
        square = number * number
        return square
    else:
        print("Le paramètre doit être un nombre !")
        return None


print(square(2))
print(square("a"))
print(square(2.5))
