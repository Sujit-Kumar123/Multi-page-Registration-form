from django.urls import path
from . import views


urlpatterns = [
    path('',views.form_one),
    path('edu/',views.form_two,name='education'),
    path('upload/',views.form_three,name='upload')
]