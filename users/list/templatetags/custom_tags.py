from django import template
from datetime import date

register = template.Library()


user_status = {
    "allowed": "Allowed",
    "blocked": "Blocked"
}

number_status = {
    "bizz": "Bizz",
    "fuzz": "Fuzz",
    "bizz_fuzz": "BizzFuzz",
    "invalid": "Not valid for BizzFuzz",
}


def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year


@register.simple_tag
def status(user):
    if user.birthday is not None:
        if calculate_age(user.birthday) < 13:
            return user_status["blocked"]
        else:
            return user_status["allowed"]


@register.simple_tag
def bizz_fuzz(user):
    number = user.random_number
    if number % 3 == 0 and number % 5 == 0:
        return number_status["bizz_fuzz"]
    elif number % 3 == 0:
        return number_status["bizz"]
    elif number % 5 == 0:
        return number_status["fuzz"]
    else:
        return number_status['invalid']




