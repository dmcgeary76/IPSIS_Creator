from django.urls import path

from . import views

app_name = 'logger'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_view, name='home'),
    path('district/', views.district_view, name='district'),
    path('<int:Custom_Org_id>/', views.org_detail, name='org_detail'),
]
