from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/<str:username>/", UserProfileDetailView.as_view(), name="username_profile"),
    path("profiles/", ListActiveUser.as_view(), name="active_user"),
]
