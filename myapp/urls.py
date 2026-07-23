from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.getemployees,name='employees'),
    path('add/',views.addemployee,name='add'),
    path('find/',views.getemployee,name='findemployee'),
    path('edit/<int:id>/',views.editemployee),
    path('delete/<int:id>/',views.deleteemployee),
]
