from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User


class UserProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "profiles/profile_detail.html"

    def userprofile(self, request, *args, **kwargs):
        username = self.kwargs.get("username")
        user_profile_name = get_object_or_404(User, username=username)
        is_me = user_profile_name == username
        context = {
            "object": user_profile_name,
            "instance": user_profile_name,
            "owner": is_me,
        }
        return render(request, context)


class ListActiveUser(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "profiles/profile_list.html"

    def ListingUser(self, request, *args, **kwargs):
        context = {"users": User.objects.filter(is_active=True)}
        return render(request, context)
