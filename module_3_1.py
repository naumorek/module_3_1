global calls
calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    string1 = str(string)
    lenth = len(string1)
    string_h = string1.upper()
    string_l = string1.lower()
    string_sum = []
    string_sum.append(lenth)
    string_sum.append(string_h)
    string_sum.append(string_l)
    count_calls()
    return string_sum


def is_contains(string, list_to_search):
    k = 0
    flag=True
    for i in list_to_search:
        string_l = string.lower()
        element_list = i
        element_list = element_list.lower()
        if string_l == element_list:
            k = k + 1
    if k >= 1:
        flag=True
    else:
        flag=False
    count_calls()
    return flag




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
