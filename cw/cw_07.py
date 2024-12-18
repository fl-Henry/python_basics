import random
import string

# Генерация случайного набора уникальных букв
def generate_random_letters(length):
    # Используем только заглавные или строчные буквы латинского алфавита
    letters = string.ascii_lowercase  # Можете изменить на string.ascii_uppercase для заглавных
    ll = random.sample(letters, length)
    l2 = []
    for x in ll:
        if x not in l2:
            l2.append(x)
    return ''.join(l2)

# Пример: генерируем набор из 6 случайных уникальных букв
random_letters = generate_random_letters(12)
print(random_letters)


letters = 'viotfnpugxys'
words = [
    "ton",
    "fig",
    "fox",
    "dog",
    "tip",
    "sin",
    "pot",
    "cat",
    "pin",
    "sung",
    "gift",
    "voting",
]