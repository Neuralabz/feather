# Error Messages
CONFIG_FILE_NOT_FOUND_MESSAGE = 'Configuration file not found'
INVALID_CONFIG_FILE_EXTENSION_MESSAGE = 'Invalid configuration file extension'
INVALID_CONFIG_FILE_FORMAT_MESSAGE = 'Invalid configuration file detected'


class ConfigError(Exception):
    pass


class InvalidConfigFileFormatError(ConfigError):
    def __init__(self):
        super().__init__(INVALID_CONFIG_FILE_FORMAT_MESSAGE)


class ConfigFileNotFoundError(ConfigError):
    def __init__(self, config_filepath):
        super().__init__(f"{CONFIG_FILE_NOT_FOUND_MESSAGE}: {config_filepath}")


class InvalidConfigExtensionError(ConfigError):
    def __init__(self, extension: str):
        super().__init__(f"{INVALID_CONFIG_FILE_EXTENSION_MESSAGE}: {extension}")
