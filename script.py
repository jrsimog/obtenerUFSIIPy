import requests
from bs4 import BeautifulSoup
import sys
import time
from datetime import datetime


now = datetime.now()
year = int(now.year)
day = int(now.day)
month = int(now.month)

if len(sys.argv) > 1:
    day = int(sys.argv[1])
if len(sys.argv) > 2:
    month = int(sys.argv[2])
if len(sys.argv) > 3:
    year = int(sys.argv[3])

url = f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

meses_nombre = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
}

print(f"Buscando UF del día {day} de {meses_nombre[month]} de {year}...")
mes = meses_nombre[month]
div_id = f"mes_{mes}"
time.sleep(1)
print(f"UF del día {day} de {mes} de {year}:")
div = soup.find('div', id=div_id)
table = div.find('table')

for row in table.find_all('tr'):
    day_columns = row.find_all('th')
    for day_column in day_columns:
        for day_table in day_column.find_all('strong'):
            if int(day_table.text.strip()) == day:
                value_column = day_column.find_next_sibling('td')
                if value_column:
                    print(value_column.text)
