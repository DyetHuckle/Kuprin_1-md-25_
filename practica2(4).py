import random


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    return expression


def check_answer(expression, user_answer):
    result = eval(expression)
    if int(user_answer) == result:
        print("Правильно!")
        return True
    else:
        print("Ответ неверный")
        return False


def math_game():
    correct_answers = 0
    wrong_answers = 0
    while wrong_answers < 3:
        expression = generate_expression()
        user_answer = input(f"{expression} = ")
        if check_answer(expression, user_answer):
            correct_answers += 1
        else:
            wrong_answers += 1
    print(f"Игра окончена. Правильных ответов: {correct_answers}")


# Запуск игры
math_game()
