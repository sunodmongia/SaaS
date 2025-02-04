from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def userprofile(request, username=None, *args, **kwargs):
    user = request.user
    user_profile_name = User.objects.get(username=username)
    return HttpResponse(f"This is user {username} - {user_profile_name.id}")