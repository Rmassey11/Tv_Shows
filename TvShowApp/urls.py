from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:ShowId>', views.show),
    path('shows/<int:ShowId>/edit', views.edit),
    path('shows/<int:ShowId>/update', views.update),
    path('shows/<int:ShowId>/delete', views.delete),
]