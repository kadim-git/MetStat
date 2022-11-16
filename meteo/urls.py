from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_meteo/', views.post_meteo ),
    path('meteost', views.meteost, name='meteost'),

    path('post_wind/', views.post_wind ),
    path('windmod', views.windmod, name='windmod'),

]
