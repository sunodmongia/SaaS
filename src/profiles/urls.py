from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.userprofile, name="username")
]