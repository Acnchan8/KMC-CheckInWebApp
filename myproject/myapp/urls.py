from django.urls import path
from . import views
from django.conf import settings
from . import views as main_views
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    # path('some_function/', views.some_function, name='some_function'),
    path('', views.loginUpdated_view, name='index'),
    path('loginUpdated/', views.loginUpdated_view, name='login'),
    path('database/', views.database_view, name='database'),
    path('database/<str:dataset>/', views.database_view, name='database_dataset'),
    path('create_student/', views.create_student_view, name='create_student'),
    path('update_student/', views.update_student_view, name='update_student'),
    path('delete_student/', views.delete_student_view, name='delete_student'),
    path('scanproceed/', views.scanproceed_view, name='scanproceed'),
    path('scansuccessful/', views.scansuccessful_view, name='scansuccessful'),
    path('scanunsuccessful/', views.scanunsuccessful_view, name='scanunsuccessful'),
    path('createstudent/', views.createstudent_view, name='createstudent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    
