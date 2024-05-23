sample_list = [1, 3, 5, 3, 7, 8, 1, 10, 12]

duplicates = []

unique_elements = set()

for element in sample_list:
    if element in unique_elements:

        if element not in duplicates:
            duplicates.append(element)
    else:

        unique_elements.add(element)
if duplicates:
    print(f"Повторяющиеся элементы: {duplicates}")
    for duplicate in duplicates:
        print(f"Повторяющийся элемент: {duplicate}")
else:
    print("Повторяющихся элементов нет")


print(f"Исходный список: {sample_list}")