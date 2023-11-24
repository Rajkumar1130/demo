from django.urls import path
from . import views

urlpatterns = [
    #login/base urls
    path('',views.home, name='home'),
    path('home/', views.home_login, name='home_login'),
    path('login/',views.login, name='login'),
    path('registration/',views.registration, name='registration'),
    path('zoo_action/', views.zoo_action, name='zoo_action'),
    
    
    #buliding's urls
    path('building/',views.building, name='building'),
    path('building/insert/', views.insert_building, name='insert_building'),
    path('building/view/', views.view_building, name='view_building'),
    path('view_building/', views.view_building, name='view_building'),
    path('select_building/', views.select_building, name='select_building'),
    path('building_action/', views.building_action, name='building_action'),
    path('update/<int:building_id>/', views.update_building, name='update_building'),
    
    
    #enclosure's urls
    path('enclosure/',views.enclosure, name='enclosure'),
    path('encolsure/insert/', views.insert_enclosure, name='insert_enclosure'),
    path('enclosure/view/', views.view_enclosure, name='view_enclosure'),
    path('select_enclosure/', views.select_enclosure, name='select_enclosure'),
    path('enclosure_action/', views.enclosure_action, name='Enclosure_action'),
    
    
    
        
]
