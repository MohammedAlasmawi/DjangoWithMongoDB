from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.hall_form,name='hall_insert'), # get and post req. for insert operation
    path('<int:id>/', views.hall_form,name='hall_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.hall_delete,name='hall_delete'),
    path('list/',views.hall_l,name='hall_l') # get req. to retrieve and display all records
]
