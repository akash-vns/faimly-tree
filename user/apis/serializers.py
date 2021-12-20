from rest_framework import serializers
from ..models import Family


class FamilyTreeSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = Family
        fields = ["id", 'first_name', 'last_name', 'mobile_number', 'email', 'address', 'child', 'parent']

    def get_child(self, obj):
        """return child data"""
        return FamilyTreeSerializer(instance=obj.get_children(), many=True, read_only=True).data

    def __init__(self, *args, **kwargs):
        user = kwargs.get('context', {}).get("user")
        super(FamilyTreeSerializer, self).__init__(*args, **kwargs)
        if user:
            self.fields["parent"].queryset = user.familytree.all()


