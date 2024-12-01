from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.game, name="game"),
]
