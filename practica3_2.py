words = []

# Бесконечный цикл для ввода слов
while True:
    word = input("Введите слово (или 'stop' для завершения): ")
    if word.lower() == 'stop':  # Прерываем цикл, если введено слово 'stop'
        break
    words.append(word)

# Соединяем слова в одну длинную строку, разделяя их пробелами
long_string = ' '.join(words)

# Выводим результат
print("Полученная строка:", long_string)