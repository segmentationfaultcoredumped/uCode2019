from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Session


# Create your views here.
class SessionsView(ListView):
    model = Session
    context_object_name = 'list_sessions'
    template_name = "data/home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SessionsView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        return context


class SessionView(DetailView):
    model = Session
    context_object_name = 'session'
    template_name = 'data/session.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SessionView, self).get_context_data(**kwargs)
        context['title'] = context['session'].name
        return context


