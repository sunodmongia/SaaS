from django.shortcuts import reverse, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.views import generic, View
from django.utils.decorators import method_decorator

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

class PasswordProtectedView(View):
    template_entry = "protected/entry.html"
    template_view = "protected/view.html"

    def get(self, request, *args, **kwargs):
        is_allowed = request.session.get('Page_access') or 0
        if is_allowed:
            return render(request, self.template_view)
        return render(request, self.template_entry)
    
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            user_sent = request.POST.get("PASSWORD") or None
        if user_sent == PASSWORD:
            is_allowed = 1
            request.session["Page_access"] = is_allowed
            return render(request, self.template_view)
        return render(request, self.template_entry)
    

    
@method_decorator(login_required(login_url=LOGIN_URL), name="dispatch")
class UserViewOnly(View):
    def get(self, request, *args, **kwargs):
        return render(request, "protected/user_only.html")

@method_decorator(staff_member_required(login_url=LOGIN_URL), name="dispatch")
class StaffViewOnly(View):
    def get(self, request, *args, **kwargs):
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
