from django import template
from datetime import date

register = template.Library()


def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year


@register.simple_tag
def status(user):
    if user.birthday is not None:
        if calculate_age(user.birthday) <= 13:
            return "blocked"
        else:
            return "allowed"



