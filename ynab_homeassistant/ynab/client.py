from typing import Type, TypeVar, Union

import jsons
import requests

from ynab_homeassistant.config.ynab_configuration import YnabConfiguration
from ynab_homeassistant.ynab.model.categories_response import CategoriesResponse
from ynab_homeassistant.ynab.model.error_response import ErrorResponse, ErrorWrapper
from ynab_homeassistant.ynab.model.response_wrapper import ResponseWrapper

T = TypeVar("T")
BASE_URL = "https://api.ynab.com/v1"


class YnabClient:
    _config: YnabConfiguration

    def __init__(self, config: YnabConfiguration):
        self._config = config

    def get_categories(self) -> CategoriesResponse:
        result = self._make_request(f"/budgets/{self._config.budget_id}/categories", CategoriesResponse)

        if isinstance(result, CategoriesResponse):
            return result

        raise Exception("GET categories failed", result.detail)

    def _make_request(self, path: str, response_cls: Type[T]) -> Union[T, ErrorResponse]:
        response = requests.get(f"{BASE_URL}{path}", headers={"Authorization": f"Bearer {self._config.access_token}"})

        if response.status_code == 200:
            return jsons.load(response.json(), ResponseWrapper[T]).data
        else:
            return jsons.load(response.json(), ErrorWrapper).error
