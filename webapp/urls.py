from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update_record'),
    path('record/<int:pk>', views.view_record, name='view_record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record')

]

