# Задание 8.
# pathlib
# Написать функцию с однострочником которая для заданной директории отдает список всех содержащихся директорий и их сайблингов.
# Результат - список таплов, где первый элемент директория, а второй список сайблингов.

from pathlib import Path
import os
def get_answer(path):
    return [(el[0], [d for d in Path(el[0]).parent.iterdir() if d != Path(el[0]) and d.is_dir()]) for el in os.walk(path) if el[0] != path]
    
    return [(el[0], [d for d in Path(el).parent.iterdir()]) for el in os.walk(path)]

if __name__ == "__main__":
    #print(Path.cwd())
    print(get_answer('/Users/user/yandex-backend-school/homework1/a'))
