class DataClass:
    LINK_RECEIVING_CURRENCY_QUOTES = 'https://www.cbr.ru/scripts/XML_daily.asp'

    required_fields_for_currency = [
        'NumCode', 'CharCode', 'Nominal', 'Name', 'Value', 'VunitRate'
    ]

    required_fields_to_receive_quotes = [
        "ValCurs", "Valute", "NumCode", "CharCode", "Nominal", "Name",
        "Value", 'VunitRate'
    ]

    char_code_currency = [
        'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'VND', 'HKD',
        'GEL', 'DKK', 'AED', 'USD', 'EUR', 'EGP', 'INR', 'IDR', 'KZT', 'CAD',
        'QAR', 'KGS', 'CNY', 'MDL', 'NZD', 'NOK', 'PLN', 'RON', 'XDR', 'SGD',
        'TJS', 'THB', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'RSD',
        'ZAR', 'KRW', 'JPY'
    ]
