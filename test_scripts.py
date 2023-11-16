"""Scripts for testing the app working."""

import requests


if __name__ == '__main__':
    def get_test_responses(field_dict, test_url):
        """
        Test app working.

        Args:
            field_dict (dict): test field data.
            test_url (str): test url.

        Returns:
            None:
        """
        for k, v in field_dict.items():
            print(f'Поле: {k}, значение: {v}')
        res = requests.post(test_url)
        print('Ответ сервера:')
        print(res.text)

    get_test_responses({
        'user_email': 'awesome_email@yandex.ru',
        'order_date': '2022-11-10'
    },
        ('http://127.0.0.1:5000/get_form'
         '?user_email=awesome@yandex.ru&order_date=2022-11-10')
    )

    get_test_responses({
        'product_title': 'Brand new product',  # 2 matches
    },
        ('http://127.0.0.1:5000/get_form'
         '?product_title=Brand new product')
    )

    get_test_responses({
        'created_at': '10.12.2024',
        'shop_title': 'Iphonya'
    },
        ('http://127.0.0.1:5000/get_form'
         '?created_at=10.12.2024&shop_title=Iphonya')
    )

    get_test_responses({
        'seller_email': 'my_email@email.ru',
        'seller_phone': '7 800 555 35 35',
    },
        ('http://127.0.0.1:5000/get_form'
         '?seller_email=my_email@email.ru&'
         'seller_phone=7 800 555 35 35')
    )

    get_test_responses({
        'seller_email': 'my_email@email.ru',
        'seller_phone': '7 800 555 35',  # wrong number
    },
        ('http://127.0.0.1:5000/get_form'
         '?seller_email=my_email@email.ru&'
         'seller_phone=7 800 555 35')
    )

    get_test_responses({
        'seller_email': 'my_email@e___l.ru',  # wrong email
        'seller_phone': '7 800 555 35 35',
    },
        ('http://127.0.0.1:5000/get_form?'
         'seller_email=my_email@___l.ru&seller_phone='
         '+7 800 555 35 35')
    )

    get_test_responses({
        'my_email': 'my_email@email.ru',  # no matches
        'seller_phone': '7 800 555 35 35',
        'created_date': '2022-11-24'
    },
        ('http://127.0.0.1:5000/get_form?my_email=my_email@email.ru'
         '&seller_phone=7 800 555 35 35&created_date=2022-11-24')
    )
