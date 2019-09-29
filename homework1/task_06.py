# Задание 6.
# Написать функцию которая ходит в api github и возвращает генератор number из закрытых issues в проекте
# microsoft/dotnet @GitHub. Использовать yield from

import requests

def get_numbers():
    page = 1
    answer = []
    while True:
        url = f'https://api.github.com/repos/microsoft/dotnet/issues?state=closed&page={page}&perpage=100'
        r = requests.get(url).json()
        if len(r) == 0:
            break
        print(r)
        numbers = [el['number'] for el in r]
        answer.extend(numbers)
        page += 1
    yield from numbers

if __name__ == "__main__":
    print(next(get_numbers()))
