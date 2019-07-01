from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class HomeView(View):
    template = 'front/index.html'
    def get(self, request):
        return render(self.template)