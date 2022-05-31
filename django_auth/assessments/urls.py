from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student),
    path('mentor/', views.mentor),
    path('Change_Sub/<int:id>', views.Change_Sub, name='Change_Sub'),
]