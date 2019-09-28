from datetime import datetime

years = [1967, 1978, 2000, 1987, 2010, 1977]
current_year = datetime.now().year
answer = [current_year - year for year in years]


#one line solution
answer = [2019 - year for year in [1967, 1978, 2000, 1987, 2010, 1977]]
