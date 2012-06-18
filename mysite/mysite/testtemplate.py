#!/usr/bin/python
from django.template import Template, Context
from django.conf import settings  ##add row 3&4 to avoid enviroment setting issue.
settings.configure()

person = {'name':'Sally', 'age':'43'}
t = Template('{{person.name.upper}} is {{person.age}} years old.')
c = Context({'person': person})
print t.render(c)
