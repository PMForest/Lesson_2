# Пользователь вводит строку из нескольких слов, разделённых
# пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.

usertails = input("Введите любые слова через пробел: ")
num = 1

for el in usertails.split():
    print(f"{num} {el[0:10]}")
    num += 1