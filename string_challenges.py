# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('a'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(word.lower().count('а')) # 15 минут потерял на то, чтобы понять какого хрена в тесте выводится 0, а не 2. Оказалось ошибка в ру "а" и en "a"  0_0


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
counter = 0
for word in sentence.split():
    counter += len(word)
print(counter / len(sentence.split()))