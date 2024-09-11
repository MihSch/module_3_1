# a = 1
# b = 3        # это глобальное пространство имен
# #print(a, b)
#
#
# def printer():
#     global a, b # теперь переменные стали глобальными
#     a = 'str'
#     b = 'str 2'
#     c = 15
#     d = 20          # это локальное прост имен
#     print(c, d, 'local')# в локальном пространстве можно обратиться к глобальному
#     print(a, b, 'global')
# print(a, b) #1 3
# printer()
# print(a, b) #str str 2


calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
