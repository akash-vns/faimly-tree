from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import IndexView, FamilyUpdateView, FamilyCreateView, FamilyDeleteView
from .apis.urls import router
app_name = "user"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("update/<int:pk>/", FamilyUpdateView.as_view(), name="family-update"),
    path("create/", FamilyCreateView.as_view(), name="family-create"),
    path("delete/<int:pk>/", FamilyDeleteView.as_view(), name="family-delete"),
    path(
        "login",
        LoginView.as_view(
            template_name="user/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "logout",
        LogoutView.as_view(next_page=settings.LOGIN_REDIRECT_URL),
        name="logout",
    ),
    path("api/", include(router.urls)),

]