# Задание 6.
# Написать функцию которая ходит в api github и возвращает генератор number из закрытых issues в проекте
# microsoft/dotnet @GitHub. Использовать yield from

import requests

def get_numbers():
    page = 1
    while True:
        url = f'https://api.github.com/repos/microsoft/dotnet/issues?state=closed&page={page}&perpage=100'
        r = requests.get(url).json()
        if len(r) == 0 or not isinstance(r, list):
            break
        numbers = [el['number'] for el in r]
        yield from numbers
        page += 1


if __name__ == "__main__":
    it = get_numbers()
    for _ in range(123):
        print(next(it), end=" ")
