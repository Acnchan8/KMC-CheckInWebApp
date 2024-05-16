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
    path('scanproceed/', views.scanproceed_view, name='scanproceed'),
    path('scansuccessful/', views.scansuccessful_view, name='scansuccessful'),
    path('scanunsuccessful/', views.scanunsuccessful_view, name='scanunsuccessful'),
    path('createstudent/', views.createstudent_view, name='createstudent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    
