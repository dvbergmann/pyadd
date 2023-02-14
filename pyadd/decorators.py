def safe_add(f):
    """
    Suppresses errors of addition functions by returning a tuple of None, error message if the decorated function
    throws an error.

    :param f: decorated funciton
    :return:
    """

    def wrapper(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception as err:
            return None, f'{err}'
        return result

    return wrapper()
