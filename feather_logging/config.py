import os

from feather_logging.enums import SupportedConfigExtension
from feather_logging.error import (
    ConfigFileNotFoundError,
    InvalidConfigFileFormatError
)

# Environment Properties
FEATHER_CONFIG_ENV_FILEPATH = 'FEATHER_CONFIG_PATH'

DEFAULT_CONFIG_FILEPATH = 'feather_config.json'


def get_extension(filepath: str) -> str:
    return os.path.splitext(filepath)[1]


def __get_config_filepath_from_env():
    if FEATHER_CONFIG_ENV_FILEPATH in os.environ:
        return os.environ.get(FEATHER_CONFIG_ENV_FILEPATH)

    if os.path.isfile(DEFAULT_CONFIG_FILEPATH):
        return DEFAULT_CONFIG_FILEPATH

    return None


def __load_json(content) -> dict:
    import json
    try:
        return json.loads(content)
    except ValueError:
        raise InvalidConfigFileFormatError


def __load_yaml(content):
    import yaml
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError:
        raise InvalidConfigFileFormatError


def __parse_config_content(filepath: str):
    # Check if the file has a supported extension
    extension = SupportedConfigExtension.from_str(get_extension(filepath))

    # Read the file's content
    with open(filepath, 'r') as file:
        content = file.read()

    # Parse the configuration content based on the file's extension
    if extension == SupportedConfigExtension.JSON:
        return __load_json(content)
    elif extension == SupportedConfigExtension.YAML:
        return __load_yaml(content)


def load_config_file_content(filepath: str = None):
    if filepath is None:
        # Try to fetch the (optional) config file path from the environment
        filepath = __get_config_filepath_from_env()

    if filepath:
        # Check if the file exists
        if os.path.isfile(filepath):
            return __parse_config_content(filepath)
        else:
            raise ConfigFileNotFoundError(filepath)
    else:
        return None
