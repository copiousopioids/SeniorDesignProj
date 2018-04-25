from django.urls import path, patterns, include, url
from . import views, settings
from django.conf.urls.static import static

app_name = 'hotspot'
urlpatterns = [
    #ex: /hotspot/
    path('', views.index, name='index'),
    #ex: /hotspot/8/
    path('<int:layout_id>/', views.layout_detail, name='layout detail'),
    #ex: /hotspot/8/edit
    path('<int:layout_id>/edit', views.layout_edit, name='edit layout'),
    #ex: /hotspot/add
    path('add/', views.layout_add, name='add layout'),
    #ex: /hotspot/add/submit
    path('submit/', views.upload_layout, name='upload layout'),
    
]
