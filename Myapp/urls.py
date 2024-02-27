from django.urls import path
from Myapp import views

urlpatterns=[
    path('',views.home, name='my_index'),
    path('contact/',views.contact, name='my_contact'),
    path('guard/', views.guard, name='my_guard'),
    path('service/', views.service, name='my_service'),
    path('service/', views.about, name='my_about'),

]