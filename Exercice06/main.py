# Fonction calculate_average
def calculate_average(numbers):
    numbers_sum = 0
    for number in numbers:
        numbers_sum += number
    average = numbers_sum / len(numbers)
    return average


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
