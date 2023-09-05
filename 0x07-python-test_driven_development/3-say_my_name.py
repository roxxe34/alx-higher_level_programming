#\!/usr/bin/python3
""" print names functions """
def say_my_name(first_name, last_name=""):
    """print names functions

    Args:
        first_name (str): firt name
        last_name (str): last name. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
