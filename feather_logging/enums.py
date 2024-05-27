from enum import Enum
import logging

from feather_logging.error import InvalidConfigExtensionError


class Level(Enum):
    """
    Enum listing all the available logging levels.
    """
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARN
    ERROR = logging.ERROR
    OFF = logging.NOTSET


LOGGING_LEVELS = [
    Level.DEBUG,
    Level.INFO,
    Level.WARN,
    Level.ERROR,
    Level.OFF
]


class SupportedConfigExtension(Enum):
    JSON = 'json'
    YAML = 'yml'

    @classmethod
    def from_str(cls, extension):
        extension = extension.lower()[1:]
        for name, member in cls.__members__.items():
            if member.value == extension:
                return member
        raise InvalidConfigExtensionError(extension)
