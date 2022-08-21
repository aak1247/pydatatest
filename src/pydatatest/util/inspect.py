import inspect


def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    for var_name, var_value in callers_local_vars:
        if var_value is var:
            return var_name
    return ""