from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "user_profile.html"

    def userprofile(self, request, *args, **kwargs):
        username = self.kwargs.get("username")
        user_profile_name = get_object_or_404(User, username=username)
        return HttpResponse(f"This is user {username} - {user_profile_name.id}")
