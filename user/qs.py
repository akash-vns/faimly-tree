"""separated qs methods"""
from .models import Family
from .const import RelationChoice


def get_family_qs_by_relation(extra_param={}, relation=None):
    """filtering the data with all relation """
    qs = Family.objects.filter(**extra_param)
    if extra_param.get("id") and relation:
        if relation == RelationChoice.cousin.value:
            qs = qs.get().get_all_cousins()
        elif relation == RelationChoice.grandparents.value:
            qs = qs.get().grandparents()
        elif relation == RelationChoice.children.value:
            qs = qs.get().get_children()
        elif relation == RelationChoice.sibling.value:
            qs = qs.get().get_siblings()
    return qs
