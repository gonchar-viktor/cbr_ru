import pytest
from data.data import DataClass
from conftest import get_currency_rates, requests_get
import allure


class TestReceivingCurrencyQuotes:

    @allure.title('проверяет, что ответ содержит какие-либо данные')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_xml_not_none(self, get_currency_rates):
        assert get_currency_rates is not None

    @allure.title('проверяет, что возвращается правильный код ответа')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_response_status_code(self):
        response = requests_get()
        assert response.status_code == 200

    @allure.title('проверяет наличие необходимых полей для валюты')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_required_fields_for_currency(self, get_currency_rates):
        required_fields = DataClass.required_fields_for_currency
        for currency in get_currency_rates.findall('Valute'):
            for field in required_fields:
                assert currency.find(field) is not None
                assert currency.find(field) in currency

    @allure.title(
        'проверяет, что в ответе есть информация о каждой валюте и её цене'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('currency', DataClass.char_code_currency)
    def test_information_about_the_currency_and_its_price(self, currency):
        response = requests_get()
        code = response.text.split(
            f'<CharCode>{currency}</CharCode>')[1].split('<Value>')[1].split(
            '</Value>')[0]
        assert code in response.text

    @allure.title('проверяет, что значения в соответствующих полях корректны')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_values_in_the_fields_are_correct(self, get_currency_rates):
        """ NumCode - является целым числом;
            CharCode - состоит только из букв;
            Nominal - является целым числом;
            Name - состоит только из букв;
            Value - является вещественным числом;
            VunitRate - является вещественным числом. """

        for currency in get_currency_rates.findall('Valute'):
            assert currency.find('NumCode').text.isdigit()
            assert currency.find('CharCode').text.isalpha()
            assert currency.find('Nominal').text.isdigit()
            assert currency.find('Name').text.replace(' ', '').replace(
                '(', '').replace(')', '').isalpha()
            assert currency.find('Value').text.replace(',', '').isdigit()
            assert currency.find('VunitRate').text.replace(',', '').isdigit()
