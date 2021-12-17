from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from utils.abstract_model import TimeStampedModel

# Create your models here.
User = get_user_model()


class Address(TimeStampedModel):
    """address model"""
    building_no = models.IntegerField()
    building_name = models.CharField(max_length=100)
    area = models.TextField()

    def __str__(self):
        return f"{self.building_no}-{self.building_name}"


class Family(TimeStampedModel):
    """family tree model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='familytree')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, related_name="families", on_delete=models.SET_NULL, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    mobile_number = PhoneNumberField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"Tree of {self.user}  {self.get_full_name}"

    ##########
    # Methods #
    ##########

    def get_siblings(self, parent=None):
        """
            :return all siblings else empty list
            where all the children are belonged to same parents
        """
        if not parent:
            parent = self.parent
        if not parent:
            return []
        return parent.children.all().exclude(id=self.id)

    def get_children(self):
        """:return all children"""
        return self.children.all()

    def get_all_ancestors(self):
        """:return all grandparents"""
        if self.parent:
            yield self.parent
            yield from self.parent.get_all_ancestors()

    def get_all_descendants(self):
        """:return children of children"""
        for child in self.get_children():
            yield child
            yield from child.get_all_descendants()

    def grandparents(self):
        """return grandparent  excluding current parent"""
        return [acc for acc in self.get_all_ancestors() if acc.id != self.parent.id]

    def get_all_cousins(self):
        """
            return all the cousin
            where the parent belong to same parents
        """
        cousin = []
        grand_parent = self.parent.parent if self.parent else None
        if grand_parent:
            for child in grand_parent.get_children():
                if child.id != self.parent.id:
                    cousin.extend(child.get_children())
        return cousin

    def get_update_url(self):
        return reverse('user:family-update', args=[self.id])

    def get_delete_url(self):
        return reverse('user:family-delete', args=[self.id])

    ################
    #  Properties  #
    ###############

    @property
    def get_full_name(self):
        """get full name """
        return f"{self.first_name} {self.last_name}"
