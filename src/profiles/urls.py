from django.urls import path
from .views import *

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="username")
]