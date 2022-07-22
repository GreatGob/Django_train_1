from django.urls import path
from . import views

#create urls here
app_name= "Companies"
urlpatterns = [
    path('', views.index , name= 'companies_index'),
    path('<int: companies_num>/', views.detail, name= 'detail'),
]
