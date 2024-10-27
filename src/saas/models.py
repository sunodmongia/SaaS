from django.db import models


class PageVisit(models.Model):
    pagevisit = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
