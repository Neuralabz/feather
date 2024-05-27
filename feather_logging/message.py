
CALL_MESSAGE_WITH_ARGS = '{0} called with args: {1}'
CALL_MESSAGE_WITH_KWARGS = '{0} called with kwargs: {1}'
CALL_MESSAGE_WITH_ARGS_AND_KWARGS = '{0} called with positional arguments: {1} and keyword arguments: {2}'
CALL_MESSAGE_WITHOUT_PARAMS = '{0} called'

RESULT_MESSAGE = '{0} returned {1}'

EXCEPTION_MESSAGE = '{0} raised an exception: {1}'


def __map_args(*args) -> str:
    return ", ".join(map(str, args))


def __map_kwargs(**kwargs) -> str:
    return __map_args(kwargs)


def build_call_message(fn_name, *args, **kwargs) -> str:
    mapped_args = None
    mapped_kwargs = None

    if args is not None and len(args) > 0:
        mapped_args = __map_args(*args)

    if kwargs is not None and len(kwargs) > 0:
        mapped_kwargs = __map_kwargs(**kwargs)

    if mapped_args is not None:
        if mapped_kwargs is not None:
            return CALL_MESSAGE_WITH_ARGS_AND_KWARGS.format(fn_name, mapped_args, mapped_kwargs)
        return CALL_MESSAGE_WITH_ARGS.format(fn_name, mapped_args)

    if mapped_kwargs is not None:
        return CALL_MESSAGE_WITH_KWARGS.format(fn_name, mapped_kwargs)

    return CALL_MESSAGE_WITHOUT_PARAMS.format(fn_name)


def build_result_message(fn_name, result, *args, **kwargs):
    return RESULT_MESSAGE.format(build_call_message(fn_name, *args, **kwargs), result)


def build_exception_message(fn_name, exception, *args, **kwargs):
    return EXCEPTION_MESSAGE.format(build_call_message(fn_name, *args, **kwargs), exception)
