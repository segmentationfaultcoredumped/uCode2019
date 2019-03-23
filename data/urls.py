from django.urls import path
from django.contrib import admin
from .views import SessionsView
from .views import SessionView

urlpatterns = [
    # path('', admin.site.urls, 'home'),
    path('admin/', admin.site.urls),
    path('home/', SessionsView.as_view(), name='home'),
    # path('home/sessions/<int:pk>', SessionView.as_view(),name='detail-session')
]