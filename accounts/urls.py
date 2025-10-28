# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .template_views import *

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    # Templates URLS
    path("login/", LoginPageView.as_view(), name="login_page"),
    path("profile/", ProfilePageView.as_view(), name="profile_page"),
]
