"""
Домашнее задание к лекции «Открытие и чтение файла, запись в файл»
"""

from pprint import pprint


def get_dict_from_file(path: str) -> dict:
    """
    Получить словарь рецептов
    """
    with open(path, "r", encoding="UTF-8") as file_read:
        all_data = file_read.read().split("\n\n")
        cook_book = {}
        for one_data in all_data:
            list_data = one_data.split("\n")
            key = list_data.pop(0)
            number = int(list_data.pop(0))
            if len(list_data) != number:
                print("Ошибка числа ингредиентов!\n")
            cook_book[key] = [{'ingredient_name': one_list[0], 'quantity': int(one_list[1]), 'measure': one_list[2]}
                              for one_list in [one_string.split(" | ") for one_string in list_data]]
        return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    """

    """
    cook_book = get_dict_from_file("recipes.txt")
    shop_list = {}
    for one_dish in dishes:
        if one_dish in cook_book:
            for one_string in cook_book[one_dish]:
                if one_string["ingredient_name"] in shop_list:
                    shop_list["ingredient_name"]["quantity"] += one_string["ingredient_name"] * person_count
                else:
                    shop_list[one_string["ingredient_name"]] = {
                        "measure": one_string["measure"],
                        "quantity": one_string["quantity"] * person_count
                    }
    return shop_list


def sorted_union_files(files: list, result_path: str) -> None:
    """
    Функция объединения файлов в порядке заданном числом срок.
    Функция не имеет ограничения по размеру файлов
    """
    temp_dict = {sum(1 for _ in open(one_file, encoding="UTF-8")): one_file for one_file in files}
    with open(result_path, "w") as file_write:
        file_write.write("")
    with open(result_path, "a") as file_write:
        for key in sorted(temp_dict.keys()):
            file_write.write(temp_dict[key] + "\n")
            file_write.write(str(key) + "\n")
            file_write.writelines(line for line in open(temp_dict[key], "r", encoding="UTF-8"))
            file_write.write("\n")


def main_1_2():
    shop_list = get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
    pprint(shop_list)


def main_3():
    files = ["sorted\\1.txt", "sorted\\2.txt", "sorted\\3.txt"]
    sorted_union_files(files, "result.txt")


if __name__ == "__main__":
    main_1_2()
    main_3()
