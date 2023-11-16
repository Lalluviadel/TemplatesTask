"""Main app."""

from db_files.db_management import TinyDbManager

from flask import Flask, request

from validators import (
    date_validate, email_validate,
    phone_validate
)

app = Flask(__name__)
test_db = TinyDbManager('./db_files/db.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    """
    Get names of forms that match the conditions or field types.

    Returns:
        list [dict] | dict: result of the form matching.
    """
    db_search_dict = dict()
    for field_name, field_value in request.args.items():
        if date_validate(field_value):
            field_type = 'date'
        elif phone_validate(field_value):
            field_type = 'phone'
        elif email_validate(field_value):
            field_type = 'email'
        else:
            field_type = 'text'
        db_search_dict[field_name] = field_type
    result = [
        {k: v} for i in test_db.filter_by_dict(
            db_search_dict) for k, v in i.items() if k == 'name'
    ]
    if not result:
        return db_search_dict
    return result


if __name__ == '__main__':
    app.run()
