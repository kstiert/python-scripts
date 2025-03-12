from dataclasses import dataclass
from typing import List
from uuid import UUID

from ynab_homeassistant.ynab.model.category import Category

@dataclass
class CategoryGroup:
    id: UUID
    name: str
    hidden: bool
    deleted: bool
    categories: List[Category]
