from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('user/login/', views.user_login, name='user_login'),
    path('poll/part-1/<int:question_id>/', views.poll_view, name='poll'),
    path('poll/part-2/<int:question_id>/', views.poll_view_2, name='poll_2'),
    path('continue/', views.continue_view, name='continue'),
    path('comment/', views.comment_view, name='comment'),
    path('complete/', views.complete_view, name='complete'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('about-us/', views.about_us, name='about-us'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
