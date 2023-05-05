from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adoptions/<int:pet_id>/', view = views.pet_detail, name='pet_detail'),
]
