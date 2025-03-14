from __future__ import annotations

from os import path

import jsons

from ynab_homeassistant.config.homeassistant_configuration import HomeassistantConfiguration
from ynab_homeassistant.config.ynab_configuration import YnabConfiguration

CONFIG_PATH = ".ynab_homeassistant/conf.json"


class Configuration:
    ynab: YnabConfiguration
    homeassistant: HomeassistantConfiguration

    @staticmethod
    def load_config_file() -> Configuration:
        with open(path.join(path.expanduser("~"), CONFIG_PATH), "r") as conf:
            json_conf = conf.read()
        return jsons.loads(json_conf, Configuration)
