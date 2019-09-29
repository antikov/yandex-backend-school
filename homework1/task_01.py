# Задание 1.
# Пара упражнений про list comprehensions
# даны года рождения
# [1967, 1978, 2000, 1987, 2010, 1977]
# посчитать сколько лет прошло с года рождения при помощи list comprehensions

from datetime import datetime

years = [1967, 1978, 2000, 1987, 2010, 1977]
current_year = datetime.now().year
answer = [current_year - year for year in years]
print(answer)

#one line solution
answer = [2019 - year for year in [1967, 1978, 2000, 1987, 2010, 1977]]
print(answer)
