import pprint

import ynab
from ynab.models.categories_response import CategoriesResponse

from ynab_homeassistant.configuration import Configuration

config = Configuration.load_config_file()
ynab_client = config.ynab.build_ynab_client()
categories_api = ynab.CategoriesApi(ynab_client)

pprint.pprint(categories_api.get_categories(config.ynab.budget_id))
