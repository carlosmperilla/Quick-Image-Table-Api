from .abstract_custom_filters import (
                                        ByAttrFilterBackend,
                                        ByRangeFilterBackend
                                     )


class ByStockAttrFilterBackend(ByAttrFilterBackend):
    """
    Filter by Stock attributes.
    """

    attrs = ['name']

class ByProductAttrFilterBackend(ByAttrFilterBackend):
    """
    Filter by Product attributes.
    """

    attrs = ['name', 'quantity', 'price']


class ByQuantityRangeFilterBackend(ByRangeFilterBackend):
    """
    Filter by quantity range.
    """

    attr = "quantity"

class ByPriceRangeFilterBackend(ByRangeFilterBackend):
    """
    Filter by price range.
    """

    attr = "price"