def get_count_char(str_):
    str_ ="".join(sorted(str_.lower().split()))
    count_char = {}
    for char in str_:
         if char.isalpha():
             count_char[char] = (str_.count(char))

    return count_char

def take_percentage(count_char):
    for n in count_char:
        count_char[n] = round(count_char[n]/len(main_str)*100, 1)
    return count_char
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

new_function = get_count_char(main_str)
percentage = take_percentage(new_function)
print(percentage)