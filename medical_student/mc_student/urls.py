from django.urls import path
from mc_student import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.medical,name='add'),
    path('showcivil/',views.showengineering,name="showcivil"),
    path('showmedical/',views.showmedical,name="showmedical"),
    path('sendemail/<int:id>',views.sendmail,name="sendmail"),
    path('multimail/',views.multimail,name="multimail"),
]