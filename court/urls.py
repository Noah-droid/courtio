from django.urls import path
from . import views

app_name = 'court_session'

urlpatterns = [
    path("", views.index, name='index'),
    path('case', views.case_list, name='case_list'),
    path('case/<int:case_id>/', views.case_detail, name='case_detail'),
    path('add_case/', views.add_case, name='add_case'),
]