from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/login/', views.user_login, name='user_login'),
    path('poll/part-1/<int:question_id>/', views.poll_view, name='poll'),
    path('poll/part-2/<int:question_id>/', views.poll_view_2, name='poll_2'),
    path('continue/', views.continue_view, name='continue'),
    path('comment/', views.comment_view, name='comment'),
    path('complete/', views.complete_view, name='complete'),
]