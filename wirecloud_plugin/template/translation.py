import re


def get_trans_index(value):
    """Checks if the string received as argument is a translation index"""
    if type(value).__name__ == "str" or type(value).__name__ == "unicode":
        index = re.match("__MSG_(?P<value>.+)__", value, re.I)
        if index:
            return index.group("value")
    return None


def replace_trans_index(index, value, text):

    return text.replace('__MSG_' + index + '__', value)