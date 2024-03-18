from typing import List

from ynab import ApiClient, Configuration

AUTHORIZATION = "Authorization"
BEARER = "Bearer"
YNAB_API = "https://api.ynab.com/v1"


class YnabConfiguration:
    access_token: str
    budget_id: str
    category_ids: List[str]

    def build_ynab_client(self) -> ApiClient:
        config = Configuration()
        config.host = YNAB_API
        config.api_key[AUTHORIZATION] = self.access_token
        config.api_key_prefix[AUTHORIZATION] = BEARER
        return ApiClient(config)
