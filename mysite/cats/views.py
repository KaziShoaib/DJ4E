from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed

"""
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)
"""

class MainView(LoginRequiredMixin, generic.ListView):
    model = Cat
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bc = Breed.objects.all().count()
        context['breed_count'] = bc
        return context

"""
class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)
"""

class BreedView(LoginRequiredMixin, generic.ListView):
    model = Breed


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    success_url = reverse_lazy('cats:all')
    fields = '__all__'


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    success_url = reverse_lazy('cats:all')
    fields = '__all__'


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all')
    fields = '__all__'


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
