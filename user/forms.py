"""register forms"""
from django import forms
from .const import RelationChoice
from .models import Family
from .qs import get_family_qs_by_relation


class FamilyFilterForm(forms.Form):
    """Family filter for to filter object with relations """
    member = forms.ModelChoiceField(queryset=Family.objects.none(), required=True)
    relation = forms.ChoiceField(choices=RelationChoice.choice(), required=True)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(FamilyFilterForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields["member"].queryset = user.familytree.all()

    def filter_qs(self):
        member = self.cleaned_data.get("member")
        relation = self.cleaned_data.get("relation")
        return get_family_qs_by_relation({"id": member.id}, relation)


class FamilyForm(forms.ModelForm):
    """family update form"""

    class Meta:
        model = Family
        fields = ["first_name", "last_name", "address", "parent", "mobile_number", "email", "user"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FamilyForm, self).__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()
        if user:
            self.fields["user"].initial = user.id
            self.fields["parent"].queryset = user.familytree.all()

