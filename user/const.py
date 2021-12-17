"""register constant or choices"""
from enum import Enum


class RelationChoice(Enum):
    """relation choice constant"""
    sibling = "sibling"
    grandparents = "grandparents"
    children = "children"
    cousin = "cousin"

    @classmethod
    def choice(cls):
        """choices"""
        choice_lst = []
        for key, val in cls.__members__.items():
            choice_lst.append((str(key), val.value))
        return choice_lst
