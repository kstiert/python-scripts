import json

from ynab_homeassistant.configuration import Configuration
from ynab_homeassistant.ynab.client import YnabClient

config = Configuration.load_config_file()
client = YnabClient(config.ynab)

print(json.dumps(client.get_categories()))