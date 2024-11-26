from django.views import View

from django.shortcuts import render


class CustomPageNotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)
    