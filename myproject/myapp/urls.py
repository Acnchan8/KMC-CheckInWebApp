from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('some_function/', views.some_function, name='some_function'),
    path('', views.login_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('database/', views.database_view, name='login'),

]
