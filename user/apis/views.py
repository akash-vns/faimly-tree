import django_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..const import RelationChoice
from ..models import Family
from .serializers import FamilyTreeSerializer
from ..qs import get_family_qs_by_relation


class FamilyFilter(django_filters.rest_framework.FilterSet):
    member = django_filters.ModelChoiceFilter(queryset=get_family_qs_by_relation(), label="member", method="filter_data")
    relation = django_filters.ChoiceFilter(choices=RelationChoice.choice(), label="relation", method="filter_data")

    def filter_data(self, queryset, name, value):
        return queryset


class FamilyViewSet(ModelViewSet):
    serializer_class = FamilyTreeSerializer
    queryset = get_family_qs_by_relation()
    permission_classes = [IsAuthenticated]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = FamilyFilter
    ordering = "-id"

    def get_queryset(self):
        qs = get_family_qs_by_relation({"user": self.request.user}).order_by(self.ordering)
        member = self.request.GET.get("member")
        relation = self.request.GET.get("relation")
        if member and relation:
            data = get_family_qs_by_relation({"id": member, "user": self.request.user}, relation)
            ids = [i.id for i in data]
            qs = get_family_qs_by_relation({"id__in": ids})
        return qs

    def get_serializer_context(self):
        context = super(FamilyViewSet, self).get_serializer_context()
        context["user"] = self.request.user
        return context
