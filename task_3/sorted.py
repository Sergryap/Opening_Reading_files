import fileinput
import os


def count_lines(file):
    """Функция ключа сортировки файлов по количеству строк"""
    file_path_num = os.path.join(file_path, file)
    with open(file_path_num, encoding="utf-8") as f:
        return sum(1 for _ in f)


def get_sort_data(file_dir, func):
    """
    Создание сортированных:
    - списка названий файлов,
    - генератора путей файлов,
    - списка количества строк в файлах
    """
    file_list = os.listdir(file_dir)
    sort_file_list = sorted(file_list, key=func)
    gen_sort_file_path = (os.path.join(file_dir, i) for i in sort_file_list)
    count_line = sorted([count_lines(f) for f in file_list])
    return gen_sort_file_path, sort_file_list, count_line


def gen_sorted_file(data_sort, new_file):
    """
    Функция генерации файла с отсортированными файлами
    data_sort - кортеж содержащий три параметра:
    0 - генератор путей файлов
    1 - список названий файлов
    2 - список количества строк в файлах
    """
    with fileinput.FileInput(files=data_sort[0], encoding="utf-8") as fr, open(new_file, 'w', encoding='utf-8') as fw:
        i = 0
        for line in fr:
            if fr.isfirstline():
                discription = f'{data_sort[1][i]}\n{data_sort[2][i]}'
                fw.write(f'\n{discription}\n')
                i += 1
            fw.write(line)


BASE_PATH = os.getcwd()
FILE_DIR = 'filestxt'
RESULT_DIR = 'result'
RESULT_FILE = 'sorted.txt'
file_path = os.path.join(BASE_PATH, FILE_DIR)
result_path = os.path.join(BASE_PATH, RESULT_DIR, RESULT_FILE)

sort_f = get_sort_data(file_path, count_lines)
gen_sorted_file(sort_f, result_path)
