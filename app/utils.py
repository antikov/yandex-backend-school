import datetime

def parse_date(datestring):
    return datetime.datetime.strptime(datestring, "%d.%m.%Y")

def get_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


if __name__ == "__main__":
    print(parse_date("29.02.2004"))
