# Задание 5.
# Написать функцию которая ходит в api github и возвращает одним списком number из закрытых issues в проекте
# microsoft/dotnet @GitHub

import requests

def get_numbers():
    page = 1
    answer = []
    while True:
        url = f'https://api.github.com/repos/microsoft/dotnet/issues?state=closed&page={page}&perpage=100'
        r = requests.get(url).json()
        # end of pages or too much requests from ip
        if len(r) == 0 or not isinstance(r, list):
            break
        numbers = [el['number'] for el in r]
        answer.extend(numbers)
        page += 1
    return answer

if __name__ == "__main__":
    print(get_numbers())
