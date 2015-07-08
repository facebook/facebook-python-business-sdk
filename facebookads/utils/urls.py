import six


def quote_with_encoding(value):
    """Quote a string that will be placed in url.
    If the string is unicode, we encode it
    to utf-8 before using `urllib.parse.quote`.
    In case it's not a string (an int for instance),
    we still try to convert it.

    Args:
            value: The string to be properly encoded.
    """
    if not isinstance(value, (six.integer_types, six.string_types)):
        raise ValueError("Cannot encode {} type.".format(type(value)))

    # handle other stuff than strings
    if isinstance(value, six.integer_types):
        value = six.text_type(value).encode('utf-8') if six.PY3 else bytes(value)

    # works with PY2 and PY3
    elif not isinstance(value, bytes):
        value = value.encode("utf-8")

    return six.moves.urllib.parse.quote(value)
