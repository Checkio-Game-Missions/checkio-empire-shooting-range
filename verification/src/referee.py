from checkio_referee import RefereeBase, representations, covercodes, ENV_NAME


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
        ENV_NAME.PYTHON: cover,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: py_repr,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation
    }
