import requests
import contextlib
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {'date_req': today}


@contextlib.contextmanager
def get_course(id_valute):
    try:
        response = requests.get(url, params=payload)
        xml = BeautifulSoup(response.content, 'lxml')
        valute = xml.find("valute", {"id": id_valute})
        valute_name = valute.find('name').text
        valute_value = valute.find("value").text
        valute_nominal = valute.find('nominal').text
        yield f' ({valute_nominal} шт.) {valute_name} cтоит(ят) {valute_value} руб.'
    except Exception:
        yield f"Не нашел"


with get_course("R01010") as currency:
    print(currency)
