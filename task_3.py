# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень).
# Напишите решения через list и через dict.

# Времена года вар 1
# usermonth = int(input("Введите номер месяца: "))
#
# if usermonth == 1 or usermonth == 2 or usermonth == 12:
#     print ('Winter')
# elif usermonth == 3 or usermonth == 4 or usermonth == 5:
#     print ('Sping')
# elif usermonth == 6 or usermonth == 7 or usermonth == 8:
#     print ('Summer')
# elif usermonth == 9 or usermonth == 10 or usermonth == 11:
#     print ('Autumn')
# else:
#     print ('Error')


# Времена года вар 2

seasons_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
        print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
        print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
        print(seasons_list[3])
else:
        print("Такого месяца не существует")