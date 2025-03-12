from uuid import UUID

from ynab_homeassistant.ynab.model.milliunit import Milliunit


class Category:
    id: UUID
    category_group_id: UUID
    category_group_name: str
    name: str
    hidden: bool
    note: str
    budgeted: Milliunit
    activity: Milliunit
    balance: Milliunit
    deleted: bool
