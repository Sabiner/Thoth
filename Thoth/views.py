
from rest_framework import viewsets
from django.shortcuts import render


class Index(viewsets.ViewSet):

    def get(self, request):
        return render(request, 'index/index.html')

    def about_me(self, request):
        return render(request, 'index/about_me.html')
