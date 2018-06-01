# -*- coding: utf-8 -*-

from functools import wraps


__author__ = 'sabiner'


def get_none_if_no_value(func):
    """
    Get value if has, or return none.
    :param func: specified function
    :return: value or none
    """
    @wraps(func)
    def wrapper(cls, *args, **kwargs):
        try:
            return func(cls, *args, **kwargs)
        except cls.DoesNotExist, e:
            return None
    return wrapper
