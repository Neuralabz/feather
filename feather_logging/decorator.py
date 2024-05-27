import functools
import logging

from feather_logging.constants import Level
from feather_logging.message import build_call_message, build_result_message


def singleton(fn):
    fn.__has_run = False

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if not fn.__has_run:
            fn(*args, **kwargs)
            fn.__has_run = True
    return wrapper


def _basic_log(_func=None, *, before=True, after=False, level=Level.INFO):
    def decorator(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):

            if before:
                logging.log(level.value, build_call_message(func.__name__, *args, **kwargs))

            result = func(*args, **kwargs)

            if after:
                if before:
                    after_message = build_result_message(func.__name__, result, *args, **kwargs)
                else:
                    after_message = build_result_message(func.__name__, result)

                logging.log(level.value, after_message)

            return result
        return inner_wrapper
    if _func is None:
        return decorator
    else:
        return decorator(_func)


def log_debug(_func, *, before=True, after=False):
    return _basic_log(_func, before=before, after=after, level=Level.DEBUG)


def log_info(_func, *, before=True, after=False):
    return _basic_log(_func, before=before, after=after, level=Level.INFO)


def log_error(_func, *, before=True, after=False):
    return _basic_log(_func, before=before, after=after, level=Level.ERROR)


def log_call(_func, *, level=Level.INFO):
    return _basic_log(_func, before=True, after=False, level=level)


def log_result(_func=None, *, level=Level.INFO):
    return _basic_log(_func, before=False, after=True, level=level)


def log_call_and_result(_func, *, level=Level.INFO):
    return _basic_log(_func, before=True, after=True, level=level)


@log_result(level=Level.ERROR)
def test(name, age=30):
    return f"Hello, {name}! {age} years"
