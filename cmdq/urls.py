from django.urls import path
from . import views


urlpatterns = [
    path('user/login/', views.user_login, name='user_login'),
    path('poll/<int:question_id>/', views.poll_view, name='poll'),
    path('complete/', views.complete_view, name='complete'),
]
