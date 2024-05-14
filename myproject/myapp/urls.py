from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('some_function/', views.some_function, name='some_function'),
    path('', views.login_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('database/', views.database_view, name='login'),
    path('create_student/', views.create_student_view, name='create_student'),
    path('students/', views.student_list_view, name='student_list'),
]
