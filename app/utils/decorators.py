import logging
from functools import wraps

from flask import current_app

def logging_decorator (func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            current_app.logger.debug(func.__name__ + " started")
            #logger.debug(func.__name__ + " started")
            return func(*args, **kwargs)
        except Exception as ex:
            current_app.logger.warning(ex)
            return {"data": None, "error": str(ex)}
        finally:
            current_app.logger.debug(func.__name__ + " finished")

    return wrapper

