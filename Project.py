#Импортируем рандинт из библиотеки random
from random import randint

#Название нашего чудо-софта
print('Innovation ContactBook\nby DENISUK')
print(' ')

#Тест на то, есть ли в директории с программой файл с именем (Names.txt)
test2 = 0
try:
  test1 = 'Наталья'
  test = open('Names.txt', 'r', encoding='windows-1251').read()
  if test1 not in test:
    pass
except FileNotFoundError:
  print('Внимание! Программа не обнаружила файла Names.txt в директории с программой')
  print(' ')
  test2 = 1
#Мой любимый чекер, переписанный с нуля 2 раза
def checker():
    checker = input('Если вы хотите продолжить, то введите 1: ')
    if checker == '1':
        print(' ')
        start_of_program()
    else:
        print(' ')
        print('Вы достаточно криворук. Поэтому мы сами вернём Вас в меню!')
        print(' ')
        start_of_program()
    checker = 0

#Словарь, в котором содержутся наши контакты
contacts = {}

#Функция поиска контакта (Функция №1)
def search():
  contact_searcher_input = input('Введите имя контакта: ')
  if contact_searcher_input in contacts:
      result = 'Номер телефона контакта ' + str(contact_searcher_input) + ': ' + str(contacts[contact_searcher_input])
      #Номер находим поиском в кортеже ключевого слова (в нашем случае имени контакта)
      print(' ')
      print(result)
      print(' ')
  else:
      print(' ')
      print('Вы ввели для поиска несуществующий контакт!')
      print(' ')
  checker()
  
#Функция добавления контакта (Функция №2)
def add_contact():
  contact_name = input('Введите имя нового контакта: ')
  contact_phone = input('Введите телефон нового контакта: ')
  new_contact = {contact_name : contact_phone}
  contacts.update(new_contact)
  print(' ')
  print('Контакт с именем ' + contact_name + ' успешно добавлен')
  print(' ')
  checker()

#Взламываем НАСА за 0.000001 секунду (Функция №3)
def hack_the_NASA():
  for counter in range(10):
    print('NASA HAS BEEN HACKED! NASA HAS BEEN HACKED! NASA HAS BEEN HACKED!')
  print(' ')
  checker()

#Функция, показывающая имена всех контактов (Функция №4)
def show_contacts():
  if ':' in str(contacts):
    print('Доступные контакты: ')
    print(' ')
    for i in contacts:
      print(i)
    print(' ')
  else:
    print('Ваша контактная книжка пуста!')
    print(' ')
  checker()

#Функция, заполняющая словарь контактами (Функция №5)
def napolnitel():
  count_of_contacts = int(input('Введите количество контактов для наполнения: '))
  file_with_names = open('Names.txt', 'r').read()
  names = file_with_names.split()  
  for counter1 in range(count_of_contacts):
    new_contact_name = names[randint(0, 1340)]
    new_contact_phone = '+' + str(randint(79000000000, 79999999999))
    new_contact_key = {new_contact_name : new_contact_phone}
    contacts.update(new_contact_key)
  print(' ')
  print('Новые контакты в количестве ' + str(count_of_contacts) + ' штук были добавлены')
  print(' ')
  checker()



#Начало программы для пользователя
def start_of_program():
  print('Доступные функции: ')
  print('1 - Найти контакт\n2 - Добавить новый контакт\n3 - Взломать НАСА\n4 - Вывести все контакты\n5 - Наполнить книгу контактов контактами')
  print(' ')
  #Переменная, в которой мы считываем желание пользователя
  wuw = input('Что ты хочешь?: ')
  if wuw == '1':
    search()
  if wuw == '2':
    add_contact()
  if wuw == '3':
    hack_the_NASA()
  if wuw == '4':
    show_contacts()
  if wuw == '5':
    if test2 != 1:
      napolnitel()
    if test2 == 1:
      print(' ')
      print('Функция наполнения не работает. В директории с программой отсутствует файл Names.txt')
      print(' ')
      checker()
  else:
      print(' ')
      print('Вы криворук. Пожалуйста введите цифру функции!')
      print(' ')
      checker()
#Запускаем наше детище
start_of_program()
