letter_scores = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}


def calculate_word_score(word):
    score = 0
    for letter in word.upper():
        score += letter_scores.get(letter, 0)  # Получаем стоимость буквы, если буква не найдена - 0
    return score


user_word = input("Введите слово: ")


word_score = calculate_word_score(user_word)
print(f"Стоимость слова '{user_word}' составляет: {word_score} очков.")