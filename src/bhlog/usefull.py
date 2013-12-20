import inspect
import logging


def current_logging_call_stack(except_modules=[]):
    """ return the call hierarchy for the current stack """
    # we need the frame where logging was called not the frame of this call
    outer = inspect.getouterframes(logging.currentframe())
    notNone = [fr for fr in outer if inspect.getmodule(fr[0])]
    excepted = [fr for fr in notNone
                if inspect.getmodule(fr[0]).__name__ not in except_modules]
    return ["{module_name}.{func_name}:{lineno}".format(
        module_name=inspect.getmodule(fr).__name__,
        func_name=func_name, lineno=lineno)
            for fr, filename, lineno, func_name, lines, index in excepted]
