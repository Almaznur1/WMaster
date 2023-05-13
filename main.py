from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime, date
import pandas
from pprint import pprint
import collections


def define_year_word(years_since_foundation):
    if 10 <= (years_since_foundation % 100) <= 19 or not years_since_foundation % 10:
        year_word = 'лет'
    elif 5 <= years_since_foundation % 10 <= 9:
        year_word = 'лет'
    elif years_since_foundation % 10 == 1:
        year_word = 'год'
    else:
        year_word = 'года'
    return year_word


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

years_since_foundation = date.today().year - datetime(year=1920, month=1, day=1).year

wines = pandas.read_excel('wine2.xlsx',
                          na_values=['N/A', 'NA'], keep_default_na=False)
wines = wines.to_dict(orient='records')

drinks = collections.defaultdict(list)
for drink in wines:
    drinks[drink['Категория']] = []
for drink in drinks:
    drinks[drink] = [wine for wine in wines if wine['Категория'] == drink]

rendered_page = template.render(years_since_foundation=years_since_foundation,
                                year_word=define_year_word(years_since_foundation),
                                drinks=drinks)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
