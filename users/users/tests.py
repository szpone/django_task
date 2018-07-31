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

    def test_render_status(self):
        birthday = date(1999, 8, 20)
        c = Context({'value': birthday})
        t = Template('{% load custom_tags %}{% status  value %}')

        rendered = t.render(c)
        self.assertEqual(rendered, "Allowed")






