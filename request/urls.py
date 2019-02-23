from django.urls import include, path
from django.conf.urls import url

from .views import (
    home,
    AddUserView,
)

urlpatterns = [
    url(r'home/$', home, name="Main view of the dashboard"),
    url(r'register/$', AddUserView.as_view(), name="Add user view")
]