n = int(input("Введите количество слов: "))

words = []


for _ in range(n):
    word = input("Введите слово: ")
    words.append(word)


long_string = ' '.join(words)

# Выводим результат
print("Полученная строка:", long_string)