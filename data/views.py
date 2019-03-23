from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from .models import Session
from .models import Athlete
from .models import AthleteVest
from .models import Sensor
from .models import SensorAthlete


# Create your views here.
class SessionsView(LoginRequiredMixin, ListView):
    model = Session
    context_object_name = 'list_sessions'
    template_name = "data/home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SessionsView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        return context


class SessionView(LoginRequiredMixin, DetailView):
    model = Session
    context_object_name = 'session'
    template_name = 'data/session.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SessionView, self).get_context_data(**kwargs)
        context['title'] = context['session'].name
        context['athletes'] = Athlete.objects.filter(session=context['session'])
        return context


class AthleteView(LoginRequiredMixin, DetailView):
    model = Athlete
    context_object_name = 'athlete'
    template_name = 'data/athlete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AthleteView, self).get_context_data(**kwargs)
        context['title'] = context['athlete'].nickname
        context['sensors_of_athlete'] = SensorAthlete.objects.filter(id_athlete=context['athlete'])
        context['vests_of_athlete'] = AthleteVest.objects.filter(id_athlete=context['athlete'])
        return context


class SensorView(LoginRequiredMixin, DetailView):
    model = Sensor
    context_object_name = 'sensor'
    template_name = 'data/sensor.html'

    def get_context_data(self, **kwargs):
        context = super(SensorView, self).get_context_data(**kwargs)
        context['title'] = context['sensor'].code
        return context


class SensorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sensor


class AthleteDeleteView(LoginRequiredMixin, DeleteView):
    model = Athlete


class SessionDeleteView(LoginRequiredMixin, DeleteView):
    model = Session


class SensorCreateView(LoginRequiredMixin, CreateView):
    model = Sensor
    fields = 'code'


class SensorAthleteInline(InlineFormSetFactory):
    model = SensorAthlete
    fields = ['id_sensor', 'position']


class AthleteVestInline(InlineFormSetFactory):
    model = AthleteVest
    fields = ['vest_num', 'time']


class AthleteCreateView(CreateWithInlinesView):
    model = Athlete
    inlines = [AthleteVestInline, SensorAthleteInline]
    fields = ['nickname', 'age', 'foot_size', 'weight', 'height', 'data_consent']
    template_name = 'data/athlete_form.html'


class SessionCreateView(LoginRequiredMixin, CreateView):
    model = Session
    fields = ['name', 'training', 'date', 'place', 'grass', 'wet', 'temp', 'hum', 'additional_info']


class SessionEditView(LoginRequiredMixin, UpdateView):
    model = Session
    fields = ['name', 'training', 'date', 'place', 'grass', 'wet', 'temp', 'hum', 'additional_info']


class AthleteEditView(UpdateWithInlinesView):
    model = Athlete
    inlines = [AthleteVestInline, SensorAthleteInline]
    fields = ['nickname', 'age', 'foot_size', 'weight', 'height', 'data_consent']
    template_name = 'data/athlete_form.html'


class SensorEditView(LoginRequiredMixin, UpdateView):
    model = Sensor
    fields = 'code'
