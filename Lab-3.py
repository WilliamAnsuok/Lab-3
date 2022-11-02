short_names = 'впбаинтофкр'
sizes = {'в': 3, 'п': 2, 'б': 2, 'а': 2, 'и': 1, 'н': 1, 'т': 3, 'о': 1, 'ф': 1, 'к': 2, 'р': 2}
values = {'в': 25, 'п': 15, 'б': 15, 'а': 20, 'и': 5, 'н': 15, 'т': 20, 'о': 25, 'ф': 15, 'к': 20, 'р': 20}
values_per_size = []
for i in short_names:
    values_per_size.append([values[i] / sizes[i], i])
values_per_size.sort()
values_per_size.reverse()

#Собираем рюкзак
def f_backpack(p):
    backpack = ['д']
    points = 30  # 20 стартовых + 10 за антидот
    short_names_new = ''
    for i in range(11):
        short_names_new += values_per_size[i][1]
    for i in short_names_new:
        if len(backpack) + sizes[i] <= p:
            for l in range(sizes[i]):
                backpack.append(i)

    #Считаем очки
    for n in short_names:
        if n in backpack:
            points += values[n]
        else:
            points -= values[n]

    if points > 0:
        print(backpack[:4])
        print(backpack[4:])
        print(points)
    else:
        print('None')

f_backpack(8)
f_backpack(7)

# Доказательство невозможности для 7ми ячеек
# Т.к. Тому нужно набрать наибольшее количество очков, то логично, что нужно брать предметы с самой высокой ценностью за
# предмет, а следовательно, посколько функция рюкзака набирает по самым большим значением, пока есть свободное место в
# рюкзааке, значит она действует оптимально, а значит, если f_backpack(7) выведет 'None', значит такое невозможно