from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime, date


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

rendered_page = template.render(years_since_foundation=years_since_foundation,
                                year_word=define_year_word(years_since_foundation))

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
