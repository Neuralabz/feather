# Feather
Feather Logging enhances standard logging capabilities with a series of decorators that allows for unobtrusive logging
statements in your code.

## Initialization

Feather has (optional) initialization code that can be triggered to tweak/augment standard logging capabilities.
This can be done in one of two ways:
- Calling `dict_config` with a valid configuration `dict` object.
- Calling `yaml_config` with the path to a YAML file containing those additional parameters you want to pass to your
logging framework.

Whatever option you choose, if any, should follow the [Logging Configuration reference](https://docs.python.org/library/logging.config.html).
This guarantees a seamless integration.

JSON Config File Example

```json
{
  "version": 1,
  "disable_existing_loggers": false,
  "formatters": {
    "standard": {
      "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    }
  },
  "handlers": {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "standard"
    },
    "file": {
      "level": "INFO",
      "class": "logging.handlers.RotatingFileHandler",
      "formatter": "standard",
      "filename": "app.log",
      "maxBytes": 5000,
      "backupCount": 3,
      "mode": "a"
    }
  },
  "root": {
    "handlers": [
      "console",
      "file"
    ],
    "level": "INFO"
  }
}
```