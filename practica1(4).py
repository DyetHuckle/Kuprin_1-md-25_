def mix_colors(color1, color2):
    if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
        print("Фиолетовый")
    elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
        print("Оранжевый")
    elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
        print("Зеленый")
    else:
        print("Ошибка: Введите два из основных цветов: красный, синий или желтый")

    # Пример использования программы


color1 = input("Введите первый цвет: ").lower()
color2 = input("Введите второй цвет: ").lower()

mix_colors(color1, color2)