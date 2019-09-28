import datetime
import json

def parse_date(datestring):
    return datetime.datetime.strptime(datestring, "%d.%m.%Y").date()

def get_current_date():
    return datetime.date.today()

def get_age(born):
    today = get_current_date()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


if __name__ == "__main__":

    print(parse_date("29.02.2004"))
    print(type(parse_date("29.02.2004")))
