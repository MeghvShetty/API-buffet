# weather 
from configparser import ConfigParser
from distutils.command.config import config
from tkinter.dnd import dnd_start

def _get_api_key():
      """Fetch the API key from your configuration file.

    Expects a configuration file named "secrets.ini" with structure:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


print(_get_api_key)

