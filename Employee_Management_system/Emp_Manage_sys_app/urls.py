from django.urls import path
from Emp_Manage_sys_app import views

urlpatterns=[
    path("",views.index,name='home'),
    path("all_emp/",views.all_emp,name='all_emp'),
    path("add_emp/",views.add_emp,name='add_emp'),
    path("remove_emp/",views.remove_emp,name='remove_emp'),
    path("filter_emp/",views.filter_emp,name='filter_emp'),
    path("delete/<int:id>/",views.delete,name='delete'),
    path("update_emp/",views.update_emp,name='update_emp'),
    path("update/<int:id>/",views.update,name='update')
]