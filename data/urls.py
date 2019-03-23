from django.urls import path
from django.contrib import admin
from .views import SessionsView
from .views import SessionView
from .views import SessionCreateView
from .views import AthleteCreateView
from .views import SensorCreateView
from .views import AthleteView


urlpatterns = [
    path('', SessionsView.as_view(), name='home'),
    path('<int:pk>', SessionView.as_view(), name='detail-session'),
    path('new/', SessionCreateView.as_view(), name='new-session'),
    path('athlete/new', AthleteCreateView.as_view(), name='new-athlete'),
    path('athlete/<int:pk>', AthleteView.as_view(), name='detail-athlete'),
    path('sensor/new', SensorCreateView.as_view(), name='new-sensor'),
    # path('sensor/<int:pk>', )
]