from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

    path('tabulation/', views.tabulation, name='tabulation'),
    path('tabulation/production_number', views.tabulation_production_number, name='tabulation_production_number'),
    path('tabulation/swimsuit', views.tabulation_swimsuit, name='tabulation_swimsuit'),
    path('tabulation/evening_gown', views.tabulation_evening_gown, name='tabulation_evening_gown'),
    path('tabulation/q_and_a', views.tabulation_q_and_a, name='tabulation_q_and_a'),
]
