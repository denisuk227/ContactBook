#Название нашего чудо-софта
print('Innovation contact searcher\nby DENISUK')
#Словарь, в котором содержутся наши контакты
contacts = {
  'Чмо-Кирюша':'+79169326664',
  'Денис-Киргиз':'+79169326667',
  'Антонина':'+79162281488'

}

#Функция поиска контакта (Функция №1)
def search():
  contact_searcher_input = input('Введите имя контакта: ')
  result = 'Номер телефона контакта ' + str(contact_searcher_input) + ': ' + str(contacts[contact_searcher_input])
  return result
  
#Функция добавления контакта (Функция №2)
def add_contact():
  contact_name = input('Введите имя нового контакта: ')
  contact_phone = input('Введите телефон нового контакта: ')
  new_contact = {contact_name : contact_phone}
  contacts.update(new_contact)
  print('Контакт с именем ' + contact_name + ' успешно добавлен')

#Начало программы для пользователя
print('Что ты хочешь, чмошник?: ')
print('1 - Найти контакт\n2- Добавить новый контактn\3 - Взломать НАСА\n4 - Вывести все контакты')

#WhatUserWant - переменная, в которой мы считываем желание пользователя

wuw = int(input())

if wuw == 1:
  print(search())
if wuw == 2:

