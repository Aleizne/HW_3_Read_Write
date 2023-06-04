# ДЗ задача №1
def create_cookboock(recipe: str) -> dict:
    with open(recipe, "rt", encoding='utf-8') as f:
        res = {}
        for line in f:
            dish_name = line.strip()
            ingridients_count = int(f.readline())
            dish = []
            for _ in range(ingridients_count):
                ingridient, ing_qtty, messure_type = f.readline().strip().split(' | ')
                dish.append(
                    {'ingredient_name': ingridient,
                     'quantity': int(ing_qtty),
                     'measure': messure_type
                     }
                )
            res[dish_name] = dish
            f.readline()
    return res


# проверим корректность заполнения
cook_book = create_cookboock('recipes.txt')
print(cook_book["Омлет"])


# ДЗ задача №2
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    res = {}
    for demand_dish in dishes:
        for item in cook_book[demand_dish]:
            if res.get(item['ingredient_name']) is None:
                res[item['ingredient_name']] = {
                    'measure': item['measure'],
                    'quantity': (person_count * item['quantity'])
                }
            else:
                res[item['ingredient_name']]['quantity'] += (person_count * item['quantity'])
    return res


# Проверим заполнения рецепта
to_buy = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)
print(to_buy)


# ДЗ задание №3


def read_into_pyobject(*file_names) -> list:
    res = []
    for file in file_names:
        with open(file, 'rt', encoding='utf-8') as file_txt:
            text = file_txt.readlines()
            res.append({'file_name': file, 'text_list': text, 'length': len(text)})
    res = sorted(res, key=lambda d: d['length'])
    return res


def pyobject_to_file(target_file: str, py_objct: list) -> None:
    with open(target_file, 'wt', encoding='utf-8') as write_file:
        for element in py_objct:
            write_file.write(element['file_name'])
            write_file.write('\n')
            write_file.write(str(element['length']))
            write_file.write('\n')
            write_file.writelines(element['text_list'])
            write_file.write('\n')


testing_item = read_into_pyobject('1.txt', '2.txt', '3.txt')
print(testing_item)
pyobject_to_file('target_file.txt', testing_item)
