from django.urls import path
from django.contrib import admin
from .views import SessionsView
from .views import SessionView

urlpatterns = [
    # path('', admin.site.urls, 'home'),
    path('admin/', admin.site.urls),
    path('sessions/', SessionsView.as_view(), name='home'),
    path('sessions/<int:pk>', SessionView.as_view(), name='detail-session')
]