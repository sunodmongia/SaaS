from .views import *
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings, urls
from .views import *
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", SignUpView.as_view(), name='signup'),

    #account specificer
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
