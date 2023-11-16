"""Field type validators."""

import re
from datetime import datetime


def date_validate(field_value):
    """
    Date string validator (DD.MM.YYYY and YYYY-MM-DD only).

    Args:
        field_value (str):
            field value to validate.
    Returns:
        bool: validation result.
    """
    try:
        datetime.strptime(field_value, '%d.%m.%Y')
    except ValueError:
        try:
            datetime.strptime(field_value, '%Y-%m-%d')
        except ValueError:
            return False
    return True


def phone_validate(field_value):
    """
    Phone string validator (+7 xxx xxx xx xx only).

    Args:
        field_value (str):
            field value to validate.
    Returns:
        bool: validation result.
    """
    phone_pattern = re.compile(r'^(\+7)([ ]\d{3}){2}([ ]\d{2}){2}$')
    if any([
        phone_pattern.match(field_value),  # '+7 800 555 35 35'
        phone_pattern.match('+' + field_value),  # '7 800 555 35 35'
        phone_pattern.match('+' + field_value[1:])  # ' 7 800 555 35 35'
    ]):
        return True
    return False


def email_validate(field_value):
    """
    Email string validator (using Django's pattern).

    Args:
        field_value (str):
            field value to validate.
    Returns:
        bool: validation result.
    """
    email_pattern = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]'
        r'|\\[\001-011\013\014\016-\177])*"'
        r')@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$', re.IGNORECASE)
    if email_pattern.match(field_value):
        return True
    return False
