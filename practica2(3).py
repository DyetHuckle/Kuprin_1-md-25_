def is_rare_word(word):
    if 'ф' in word.lower():  # Проверяем наличие буквы "ф" в слове, игнорируя регистр
        return True
    else:
        return False

    # Программа запрашивает ввод слов у пользователя до тех пор, пока он не введет "стоп"


while True:
    user_input = input("Введите слово (для завершения введите 'стоп'): ")
    if user_input.lower() == "стоп":
        break
    if is_rare_word(user_input):
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")