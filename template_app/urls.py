from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('show/', views.show),
    path('student/', views.student),
    path('listemployee',views.list_employee),
    path('employee',views.add_employee),
    path('insertemployee',views.insert_employee),
    path('delete_employee/<int:myid>',views.delete_employee),
    path('edit_employee/<int:myid>',views.edit_employee),
    path('updateemployee/<int:myid>',views.update_employee) 
]
