from checkio_referee import RefereeBase, representations


import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(*[tuple(x) for x in data])
"""


def py_repr(f, data):
    return "{}({})".format(f, ", ".join(str(tuple(x)) for x in data))


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "shot"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": py_repr,
        "python_3": py_repr,
        "javascript": representations.unwrap_arg_representation
    }
