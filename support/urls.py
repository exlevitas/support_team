from django.conf.urls import url
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import *
from . import views
from .views import *

app_name = 'support'

urlpatterns = [
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='show_one_ticket'),
    path('', views.TicketFormView, name='main'),
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]