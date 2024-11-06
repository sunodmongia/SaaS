from django.shortcuts import reverse, render, redirect
from django.contrib.auth import logout
from django.views import generic
from .models import PageVisit
import pathlib
from .forms import *

this_dir = pathlib.Path(__file__).resolve().parent


class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context


def logout_view(request):
    logout(request)
    return redirect("login")


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = UserRegistrationForm

    def get_contect_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SignUp"
        return context

    def get_success_url(self):
        return reverse("login")



# def home_page(request, *args, **kwargs):
#     qs = Visitpage.objects.all()
#     page_qs = Visitpage.objects.filter(path=request.path)
#     context = {
#         "page_count": qs.count(),
#         "path_count": page_qs.count(),
#     }
#     path = request.path
#     print(f"path: {path}")
#     Visitpage.objects.create(path=request.path)
#     return render(request, "home.html", context)
