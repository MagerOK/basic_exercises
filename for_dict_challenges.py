# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_names = {}
for name in students:
    if name['first_name'] not in count_names:
        count_names.setdefault(name['first_name'], 1)
    else:
        count_names[name['first_name']] += 1
for name, count in count_names.items():
    print(f'{name}: {count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
count_names = {}
for name in students:
    if name['first_name'] not in count_names:
        count_names.setdefault(name['first_name'], 1)
    else:
        count_names[name['first_name']] += 1
max_name = max(count_names, key=count_names.get)
print(f'Самое частое имя среди учеников: {max_name}')
    

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
count_names = {}
for i, class_ in zip(range(1, len(school_students) + 1), school_students):
    count_names = {}
    for name in class_:    
        if name['first_name'] not in class_:
            count_names.setdefault(name['first_name'], 1)
        else:
            count_names[name['first_name']] += 1

    max_name = max(count_names, key=count_names.get)
    print(f'Самое частое имя в классе {i}: {max_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_ in school:
    boys_count, girls_count = 0, 0
    for member in class_['students']:
        if is_male[member['first_name']]:
            boys_count += 1
        else:
            girls_count += 1
    print(f"Класс {class_['class']}: девочки {girls_count}, мальчики {boys_count}") 


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
gender_count = {}
for class_ in school:
    boys_count, girls_count = 0, 0
    for student in class_['students']:
        if is_male[student['first_name']]:
            boys_count += 1
        else:
            girls_count += 1
    gender_count[class_['class']] = (boys_count, girls_count)
max_boys_class = max(gender_count, key=lambda x: gender_count[x][0])
max_girls_class = max(gender_count, key=lambda x: gender_count[x][1])
    
print(f"Больше всего мальчиков в классе {max_boys_class}")
print(f"Больше всего девочек в классе {max_girls_class}") 

