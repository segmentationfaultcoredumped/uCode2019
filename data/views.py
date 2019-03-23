from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Session


# Create your views here.
class SessionsView(ListView):
    model = Session
    context_object_name = 'context'
    template_name = '/data/home.html'


class SessionView(DetailView):
    model = Session
    context_object_name = 'context'
    template_name = '/data/session.html'
