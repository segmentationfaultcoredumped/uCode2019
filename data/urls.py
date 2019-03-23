from django.urls import path
from .views import SessionsView
from .views import SessionView

urlpatterns = [
    # path('', admin.site.urls, 'home'),
    path('home/', SessionsView.as_view(), 'home'),
    path('home/sessions/<int:pk>', SessionView.as_view(),'detail-session')
]