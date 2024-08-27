from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]
