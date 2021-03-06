from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view({"get": "list", "post": "create"}), name='index'),
    path('teacher/', views.TeacherListView.as_view({"get": "list", "post": "create"}), name='teachers'),
]