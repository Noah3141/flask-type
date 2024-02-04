

from typing import Literal, TypedDict, Any

from typing import Union
from datetime import timedelta as Timedelta

ConfigKey = Literal[
    "DEBUG",
    "TESTING",
    "PROPAGATE_EXCEPTIONS",
    "SECRET_KEY",
    "PERMANENT_SESSION_LIFETIME",
    "USE_X_SENDFILE",
    "SERVER_NAME",
    "APPLICATION_ROOT",
    "SESSION_COOKIE_NAME",
    "SESSION_COOKIE_DOMAIN",
    "SESSION_COOKIE_PATH",
    "SESSION_COOKIE_HTTPONLY",
    "SESSION_COOKIE_SECURE",
    "SESSION_COOKIE_SAMESITE",
    "SESSION_REFRESH_EACH_REQUEST",
    "MAX_CONTENT_LENGTH",
    "SEND_FILE_MAX_AGE_DEFAULT",
    "TRAP_BAD_REQUEST_ERRORS",
    "TRAP_HTTP_EXCEPTIONS",
    "EXPLAIN_TEMPLATE_LOADING",
    "PREFERRED_URL_SCHEME",
    "TEMPLATES_AUTO_RELOAD",
    "MAX_COOKIE_SIZE"
]







class FlaskConfig(TypedDict, total=False):
    DEBUG: bool
    TESTING: bool
    PROPAGATE_EXCEPTIONS: bool
    SECRET_KEY: str
    PERMANENT_SESSION_LIFETIME: Timedelta
    USE_X_SENDFILE: bool
    SERVER_NAME: str
    APPLICATION_ROOT: str
    SESSION_COOKIE_NAME: str
    SESSION_COOKIE_DOMAIN: str
    SESSION_COOKIE_PATH: str
    SESSION_COOKIE_HTTPONLY: bool
    SESSION_COOKIE_SECURE: bool
    SESSION_COOKIE_SAMESITE: bool
    SESSION_REFRESH_EACH_REQUEST: bool
    MAX_CONTENT_LENGTH: int
    SEND_FILE_MAX_AGE_DEFAULT: Any
    TRAP_BAD_REQUEST_ERRORS: Any
    TRAP_HTTP_EXCEPTIONS: Any
    EXPLAIN_TEMPLATE_LOADING: Any
    PREFERRED_URL_SCHEME: Any
    TEMPLATES_AUTO_RELOAD: Any
    MAX_COOKIE_SIZE: Any


#  {
#             "DEBUG": None,
#             "TESTING": False,
#             "PROPAGATE_EXCEPTIONS": None,
#             "SECRET_KEY": None,
#             "PERMANENT_SESSION_LIFETIME": timedelta(days=31),
#             "USE_X_SENDFILE": False,
#             "SERVER_NAME": None,
#             "APPLICATION_ROOT": "/",
#             "SESSION_COOKIE_NAME": "session",
#             "SESSION_COOKIE_DOMAIN": None,
#             "SESSION_COOKIE_PATH": None,
#             "SESSION_COOKIE_HTTPONLY": True,
#             "SESSION_COOKIE_SECURE": False,
#             "SESSION_COOKIE_SAMESITE": None,
#             "SESSION_REFRESH_EACH_REQUEST": True,
#             "MAX_CONTENT_LENGTH": None,
#             "SEND_FILE_MAX_AGE_DEFAULT": None,
#             "TRAP_BAD_REQUEST_ERRORS": None,
#             "TRAP_HTTP_EXCEPTIONS": False,
#             "EXPLAIN_TEMPLATE_LOADING": False,
#             "PREFERRED_URL_SCHEME": "http",
#             "TEMPLATES_AUTO_RELOAD": None,
#             "MAX_COOKIE_SIZE": 4093,
#         }















