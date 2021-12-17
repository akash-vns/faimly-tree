""" register view here"""
from django.shortcuts import render
from django.conf import settings
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FamilyFilterForm, FamilyForm
from .qs import get_family_qs_by_relation
from django.contrib import messages


# Create your views here.


class IndexView(ListView):
    template_name = "family/index.html"
    form_class = FamilyFilterForm
    paginate_by = settings.LIST_PAGE_SIZE
    ordering = "-id"
    context_object_name = "family"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ListView, self).get_context_data(
            *args, object_list=None, **kwargs
        )
        context["filter_form"] = self.get_filter_form()
        return context

    def get_filter_form(self):
        data = self.request.GET if len(self.request.GET.keys()) > 0 else None
        if len(self.request.GET.keys()) == 1 and self.request.GET.get("page"):
            # handle page parameters
            data = None
        return self.form_class(data=data, user=self.request.user)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return get_family_qs_by_relation().none()
        qs = get_family_qs_by_relation({"user": self.request.user}).order_by(self.ordering)
        filter_form = self.get_filter_form()
        if filter_form.is_bound and filter_form.is_valid():
            qs = filter_form.filter_qs()
        return qs


class FormErrorMessageMixin:
    success_message = "Data successfully submitted"
    error_message = "Please correct error below."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, self.error_message)
        return super().form_invalid(form)


class FamilyUpdateView(LoginRequiredMixin, FormErrorMessageMixin, UpdateView):
    """update family member details"""
    form_class = FamilyForm
    template_name = "family/update.html"
    queryset = get_family_qs_by_relation({})

    def get_success_url(self):
        return self.object.get_update_url()

    def get_form_kwargs(self):
        context = super().get_form_kwargs()
        context.update({"user": self.request.user})
        return context


class FamilyCreateView(LoginRequiredMixin, FormErrorMessageMixin, CreateView):
    """Create family members"""
    form_class = FamilyForm
    template_name = "family/create.html"
    success_url = "/"

    def get_form_kwargs(self):
        context = super(FamilyCreateView, self).get_form_kwargs()
        context.update({"user": self.request.user})
        return context


class FamilyDeleteView(DeleteView):
    queryset = get_family_qs_by_relation({})
    success_url = "/"

    def get(self, request, *args, **kwargs):
        messages.success(self.request, "Data deleted successfully.")
        return self.post(request, *args, **kwargs)
