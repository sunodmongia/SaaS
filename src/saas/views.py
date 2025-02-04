from django.shortcuts import reverse, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.views import generic
from .models import PageVisit
import pathlib
from .forms import *

this_dir = pathlib.Path(__file__).resolve().parent


LOGIN_URL = settings.LOGIN_URL

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


PASSWORD = "7374wire"


def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get("Page_access") or 0
    if request.method == "POST":
        user_sent = request.POST.get("PASSWORD") or None
        if user_sent == PASSWORD:
            is_allowed = 1
            request.session["Page_access"] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html")
    return render(request, "protected/entry.html")


@login_required(login_url=LOGIN_URL)
def UserViewOnly(request, *args, **kwargs):
    return render(request, "protected/user_only.html")

@staff_member_required(login_url=LOGIN_URL)
def StaffViewOnly(request, *args, **kwargs):
    return render(request, "protected/staff_only.html")


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
