import dpath

def get_config(params, key):
    """
    prototype config storage
    PEP-8 violations during dev-phase, it's easier to move funcs around with imports
    :param key:
    :return:
    """


    return dpath.get(params, key, '_')