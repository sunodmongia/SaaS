from django.db import models


class Visitpage(models.Model):
    pagevisit = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
