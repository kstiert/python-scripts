from typing import List

from ynab_homeassistant.ynab.model.category_group import CategoryGroup

class CategoriesResponse:
    category_groups: List[CategoryGroup]
    server_knowledge: int

class CategoriesResponseWrapper:
    data: CategoriesResponse
