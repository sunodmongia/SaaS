from django.shortcuts import reverse, render
from django.views import generic
from .models import Visitpage
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


class HomeView(generic.TemplateView):
    template_name = "home.html"
    get_context_data = "temp"

    def get_queryset(self):
        queryset = Visitpage.objects.all()
        # queryset = queryset.order_by("-timestamp")
        # queryset = queryset[:5]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context


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
