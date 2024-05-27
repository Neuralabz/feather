import logging
import logging.config

from feather_logging.config import load_config_file_content
from feather_logging.decorator import singleton


def dict_config(conf):
    logging.config.dictConfig(conf)


@singleton
def file_config(filepath: str):
    dict_config(load_config_file_content(filepath))


@singleton
def auto_conf():
    additional_config = load_config_file_content()
    if additional_config:
        dict_config(additional_config)


auto_conf()
