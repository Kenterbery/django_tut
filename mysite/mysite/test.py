from django.template import Template, Context
import datetime

d = datetime.date(1993, 5, 2)
t = Template('The month is {{ date.month }} and the year is {{ date.year }}')
c = Context({"date" : d})
print(t.render(c))