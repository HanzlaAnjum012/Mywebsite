from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links', views.links, name='/links'),
    path('project', views.project, name='/projects'),
    path('contact', views.contact, name="/contact")
]
