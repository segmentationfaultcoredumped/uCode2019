from django.urls import path
from django.contrib import admin
from .views import SessionsView
from .views import SessionView

urlpatterns = [
    path('', SessionsView.as_view(), name='home'),
    path('<int:pk>', SessionView.as_view(), name='detail-session')
]