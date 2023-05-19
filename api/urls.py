from django.urls import path
from api.views import find_two_points_closest

urlpatterns = [
    path('points', find_two_points_closest, name='points'),
]
