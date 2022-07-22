from django.urls import path
from . import views
app_name= 'list'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:company_id>/', views.details, name='details-company'),
    path('<int:company_id>/results/', views.employees, name='employees'),
    # path('<int:company_id>/results/<int:employee_id>/'),
]
