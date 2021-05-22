from django.urls import path
from . import views
app_name='home'
urlpatterns=[
    path('',views.home,name='home'),
    path('allimages/',views.all_images,name='image'),
    path('api/<int:id>/',views.api_service,name='api'),
]