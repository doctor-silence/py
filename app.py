

user1 = {'name': 'Иван', 'age': 20, 'account': {'login': 'ivan', 'password': 'q1'}}
user2 = {'name': 'Петр', 'age': 25, 'account': {'login': 'petr', 'password': 'q2'}}
user3 = {'name': 'Ольга', 'age': 18, 'account': {'login': 'olga', 'password': 'q3'}}
user4 = {'name': 'Анна', 'age': 27, 'account': {'login': 'anna', 'password': 'q4'}}


user_list = [user1, user2, user3, user4]


user_key = input('Введите ключ (name или account): ').lower()

try:
  
  print(f'значение ключа {user_key} для юзера 1 = {user1[user_key]}')
  print(f'значение ключа {user_key} для юзера 2 = {user2[user_key]}')
  print(f'значение ключа {user_key} для юзера 3 = {user3[user_key]}')
  print(f'значение ключа {user_key} для юзера 4 = {user4[user_key]}')
except KeyError:

  print('Введенный ключ не найден')



number = input('Введите порядковый номер: ')
print(f'Данные по юзеру № {number}:')


user = user_list[int(number)-1]


print(f"имя: {user['name']}")
print(f"возраст: {user['age']}")
print(f"логин: {user['account']['login']}")
print(f"пароль: {user['account']['password']}")



number = input('Введите номер пользователя, которого нужно переместить в конец: ')

print('Список до изменения:')
print(user_list)


item_pop = user_list.pop(int(number)-1)
print(f"Пользователь с именем {item_pop['name']} перемещен в конец")


user_list.append(item_pop)
print('Список после изменения:')
print(user_list)