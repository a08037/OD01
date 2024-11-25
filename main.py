# Функция для проверки, является ли строка палиндромом
def is_palindrome(string):
    # Шаг 1: Привести строку к единому регистру
    string = string.lower()

    # Шаг 2: Удалить пробелы и знаки пунктуации
    string = ''.join(char for char in string if char.isalnum())

    # Шаг 3: Сравнить строку с её перевёрнутой версией
    if string == string[::-1]:
        return True  # Строка является палиндромом
    else:
        return False  # Строка не является палиндромом


# Запрос ввода у пользователя
user_input = input("Введите строку для проверки на палиндром: ")

# Вызов функции и вывод результата
if is_palindrome(user_input):
    print(f'"{user_input}" является палиндромом.')
else:
    print(f'"{user_input}" не является палиндромом.')
