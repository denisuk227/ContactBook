#Название нашего чудо-софта
print('Innovation ContactBook\nby DENISUK')
print(' ')
#Словарь, в котором содержутся наши контакты
contacts = {
  'Кирюша':'+79169326664',
  'Денис-Киргиз':'+79169326667',
  'Антонина':'+79162281488'

}

#Функция поиска контакта (Функция №1)
def search():
  contact_searcher_input = input('Введите имя контакта: ')
  result = 'Номер телефона контакта ' + str(contact_searcher_input) + ': ' + str(contacts[contact_searcher_input])
  print(' ')
  print(result)
  print(' ')
  checker1 = int(input('Хочешь сделать ещё что-нибудь? Введи 1: '))
  print(' ')
  if checker1 == 1:
    start_of_program()
  checker1 = 0
  
#Функция добавления контакта (Функция №2)
def add_contact():
  contact_name = input('Введите имя нового контакта: ')
  contact_phone = input('Введите телефон нового контакта: ')
  new_contact = {contact_name : contact_phone}
  contacts.update(new_contact)
  print(' ')
  print('Контакт с именем ' + contact_name + ' успешно добавлен')
  print(' ')
  checker2 = int(input('Хочешь сделать ещё что-нибудь? Введи 1: '))
  print(' ')
  if checker2 == 1:
    start_of_program()
  checker2 = 0

#Взламываем наса за 0.000001 секунду (Функция №3)
def hack_the_NASA():
  for counter in range(10):
    print('NASA HAS BEEN HACKED!')
  print(' ')
  checker4 = int(input('Хочешь сделать ещё что-нибудь? Введи 1: '))
  print(' ')
  if checker4 == 1:
    start_of_program()
  checker4 = 0

#Функция, показывающая имена всех контактов (Функция №4)
def show_contacts():
  print('Доступные контакты: ')
  print(' ')
  for i in contacts:
    print(i)
  print(' ')
  checker3 = int(input('Хочешь сделать ещё что-нибудь? Введи 1: '))
  print(' ')
  if checker3 == 1:
    start_of_program()
  checker3 = 0



#Начало программы для пользователя
def start_of_program():
  print('Что ты хочешь?: ')
  print('1 - Найти контакт\n2 - Добавить новый контакт\n3 - Взломать НАСА\n4 - Вывести все контакты')
  #Переменная, в которой мы считываем желание пользователя
  wuw = int(input())
  if wuw == 1:
    search()
  if wuw == 2:
    add_contact()
  if wuw == 3:
    hack_the_NASA()
  if wuw == 4:
    show_contacts()
  checker4 = int(input('Хочешь сделать ещё что-нибудь? Введи 1: '))
  print(' ')
  if checker4 == 1:
    start_of_program()
  checker4 = 0


#Запускаем наше детище
start_of_program()
