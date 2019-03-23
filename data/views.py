from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Session
from .models import Athlete
from .models import AthleteVest
from .models import Sensor
from .models import SensorAthlete


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
        context['athletes'] = Athlete.objects.filter(session=context['session'])
        return context


class AthleteView(DetailView):
    model = Athlete
    context_object_name = 'athlete'
    template_name = 'data/athlete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SessionView, self).get_context_data(**kwargs)
        context['title'] = context['athlete'].nickname
        context['sensors_of_athlete'] = SensorAthlete.objects.filter(id_athlete=context['athlete'])
        return context

class SensorDeleteView(DeleteView):
    pass


class AthleteDeleteView(DeleteView):
    pass


class SessionDeleteView(DeleteView):
    pass


class SensorCreateView(CreateView):
    pass


class AthleteCreateView(CreateView):
    pass


class SessionCreateView(CreateView):
    pass


class SessionEditView(UpdateView):
    pass


class AthleteEditView(UpdateView):
    pass


class SensorEditView(UpdateView):
    pass


class SessionUpdateView(UpdateView):
    pass