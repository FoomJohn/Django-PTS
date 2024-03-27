from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('candidate/<int:pk>', views.candidate_record, name='candidate'),
    path('delete/<int:pk>', views.delete_candidate, name='delete_candidate'),
    path('add_candidate/', views.add_candidate, name='add_candidate'),
    path('update_candidate/<int:pk>', views.update_candidate, name='update_candidate'),
    path('score_candidate/<int:pk>', views.score_candidate, name='score_candidate'),

    path('tabulation/', views.tabulation, name='tabulation'),
    path('tabulation/production_number', views.tabulation_production_number, name='tabulation_production_number'),
    path('tabulation/swimsuit', views.tabulation_swimsuit, name='tabulation_swimsuit'),
    path('tabulation/evening_gown', views.tabulation_evening_gown, name='tabulation_evening_gown'),
    path('tabulation/q_and_a', views.tabulation_q_and_a, name='tabulation_q_and_a'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)