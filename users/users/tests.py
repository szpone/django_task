from unittest import TestCase
from django.template import Context, Engine, Template
from datetime import date
from list.templatetags.custom_tags import calculate_age
from list.models import User



class CustomTemplateTagTest(TestCase):

    def test_calculate_age(self):
        birthday = date(1999, 9, 20)
        result = calculate_age(birthday)

        self.assertEqual(result, 19)

    def test_render_allowed(self):
        birthday = date(1999, 8, 20)
        c = Context({'value': birthday})
        t = Template('{% load custom_tags %}{% status  value %}')

        self.assertEqual(t.render(c), "Allowed")

    def test_render_blocked(self):
        birthday = date(2010, 8, 20)
        c = Context({'value': birthday})
        t = Template('{% load custom_tags %}{% status  value %}')

        self.assertEqual(t.render(c), "Blocked")

    def test_fuzz(self):
        c = Context({"value": 5})
        t = Template('{% load custom_tags %}{% bizz_fuzz value %}')

        self.assertEqual(t.render(c), "Fuzz")

    def test_bizz(self):
        c = Context({"value": 3})
        t = Template('{% load custom_tags %}{% bizz_fuzz value %}')

        self.assertEqual(t.render(c), "Bizz")

    def test_bizz_fuzz(self):
        c = Context({"value": 15})
        t = Template('{% load custom_tags %}{% bizz_fuzz value %}')

        self.assertEqual(t.render(c), "BizzFuzz")







