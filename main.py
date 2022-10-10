import os
curent = os.getcwd()
folder_name = 'files'
file_name = 'recept.txt'
full_path = os.path.join(curent, folder_name, file_name)

"""     Задание номер 1     """


def generate_recept(full_path, name='file', mode= 'rt', encode='utf-8'):
    """
    На вход подается файл с рецептами блюд или с похожей структурой данных, функция
    преобразует текст в словарь, где ключами являются названия блюд, а значениями списки с рецептами

    :param full_path:
    :param name:
    :param mode:
    :param encode:
    :return:
    """
    cook_book = {}

    with open(full_path, 'rt', encoding='utf8') as file:
        for l in file:
            dish_name = l.strip()
            cook_book[dish_name] = []
            count_engr = file.readline()
            for el in range(1, int(count_engr) + 1):
                rec = file.readline().strip().split(' | ')
                ingr, quant, meas = rec
                cook_book[dish_name].append({
                        'ingredient_name': ingr,
                        'quantity': int(quant),
                        'measure': meas
                    })
            file.readline()
    return cook_book





"""     Задание номер 2     """
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2


def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция возвращает словарь в котором ключами являются ингридиенты блюд
    (Названия блюд подаются на вход и берутся из функции generate_recept())
    А значениями являются ед.измерения тех блюд + нужное количество исходя из кол-ва персон
    :param dishes:
    :param person_count:
    :return:
    """
    result = {}
    for dish in dishes:
        recipes_by_name = generate_recept(full_path)[dish]
        for recept in recipes_by_name:
            ingridient = recept['ingredient_name']
            recept.pop('ingredient_name')
            new_recepts = {
                'measure': recept['measure'],
                'quantity': recept['quantity']*person_count
            }
            result[ingridient] = new_recepts
    return result


"""     Задача номер 3      """

def func(directory, file_name ):
    with open(f'{directory}/{file_name}', 'rt', encoding='utf8') as file:
        text = file.read()  # Здесь общий текст документа
        count_list = text.split('\n')  # Здесь список со строками для подсчета
        number_of_lines = len(count_list)  # Здесь количество строк
        return file_name, number_of_lines, text.split('\n')


second_curent = os.getcwd()
writing_folder_name = 'files'
file_name = 'writing.txt'
full_path_second = os.path.join(curent, folder_name, file_name)


with open(full_path_second, 'w', encoding='utf8') as file_write:

    first_txt = func('third_work', '1.txt')
    second_txt = func('third_work', '2.txt')
    third_txt = func('third_work', '3.txt')

    name = None
    count_string = None
    text = None

    document_list = [first_txt, second_txt, third_txt]
    sorted_document__lists = sorted(document_list, key=lambda count: count[1])

    for document in sorted_document__lists:
        name, count_string, text = document
        file_write.write(f'{name}\n')
        file_write.write(f'{str(count_string)}\n')
        for strings in text:
            file_write.write(f'{strings}\n')





''' Полностью рабочий код'''
# first_txt = func('third_work', '1.txt')
# second_txt = func('third_work', '2.txt')
# third_txt = func('third_work', '3.txt')
# document_list = [first_txt, second_txt, third_txt]
# sorted_document__lists = sorted(document_list, key=lambda count: count[1])
# name = None
# count_string = None
# text = None
# for document in sorted_document__lists:
#     name, count_string, text = document
#     print(name)
#     print(count_string)
#     for strings in text:
#         print(strings)

''' Возвращает данные в том виде в котором надо, но без сортировки'''
# lists = [first_txt, second_txt, third_txt]
#
# a = None
# b = None
# c = None
# for i in lists:
#     a, b, c = i
#     print(a)
#     print(b)
#     for m in c:
#         print(m)


