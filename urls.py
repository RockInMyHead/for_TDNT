from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView

from .  import views

app_name = 'general_web'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>', views.topic, name = 'topic'),
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('writers/', views.writers, name='writers'),
    path('writer/<str:file_name>', views.writer, name = 'writer'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]