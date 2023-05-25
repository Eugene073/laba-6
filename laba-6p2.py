"""В меню кафе 10 разных типов десертов. Сформировать (вывести) все возможные варианты десертов для 3 девушек."""

desserts = [{'name': 'десерт №1', 'calories': 200},
            {'name': 'десерт №2', 'calories': 300},
            {'name': 'десерт №3', 'calories': 150},
            {'name': 'десерт №4', 'calories': 250},
            {'name': 'десерт №5', 'calories': 350},
            {'name': 'десерт №6', 'calories': 180},
            {'name': 'десерт №7', 'calories': 280},
            {'name': 'десерт №8', 'calories': 220},
            {'name': 'десерт №9', 'calories': 320},
            {'name': 'десерт №10', 'calories': 120}]

# создание списка девушек
girls = ['1-ая девушка', '2-ая девушка', '3-ая девушка']

# создание списка всех возможных комбинаций десертов
combinations = []
for i in range(len(desserts)):
    for j in range(len(desserts)):
        for k in range(len(desserts)):
            combination = [desserts[i], desserts[j], desserts[k]]
            if combination not in combinations:
                combinations.append(combination)

# ограничение на калорийность
mcol = 700
filtered_combinations = [combination for combination in combinations if sum(dessert['calories'] for dessert in combination) <= mcol]

# целевая функция - максимизация количества десертов
def dessert_count(combination):
    count = 0
    for desserts in combination:
        count += 1
    return count

# сортировка по целевой функции
filtered_combinations = sorted(filtered_combinations, key=dessert_count, reverse=True)

# вывод результата
count = len(filtered_combinations)
for i, combination in enumerate(filtered_combinations):
    print("Вариант №", i+1, "- количество десертов:", dessert_count(combination))
    for girl, dessert in zip(girls, combination):
        print(girl, 'будет есть', dessert['name'], '({} ккал)'.format(dessert['calories']))
    print('-' * 20)

print("Итоговое количество вариантов:", count)


