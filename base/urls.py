from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('service-details1/', views.service_details1, name = 'service-details1'),
    path('service-details2/', views.service_details2, name = 'service-details2'),
    path('service-details3/', views.service_details3, name = 'service-details3'),
    path('service-details4/', views.service_details4, name = 'service-details4'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('contact/', views.contact, name = 'contact'),
]