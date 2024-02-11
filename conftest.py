import allure
import pytest
import xml.etree.ElementTree as ET
import requests
from data.data import DataClass


@pytest.fixture(scope='function')
@allure.title('возвращает обработанный XML-элемент')
def get_currency_rates():
    response = requests_get()
    return ET.fromstring(response.content)


@allure.title('запрос')
def requests_get():
    """
    Чтобы получить документ на определённую дату,
    нужно заполнить параметр "date_req" используя формат - str: "dd/mm/yyyy"
    """
    date_req = None
    if date_req is None:
        return requests.get(DataClass.LINK_RECEIVING_CURRENCY_QUOTES)
    else:
        return requests.get(
            f'{DataClass.LINK_RECEIVING_CURRENCY_QUOTES}?date_req={date_req}')
