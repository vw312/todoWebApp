from django.urls import path,include
from .views import create_schedule,delete_schedule,edit_schedule,scheduleList

urlpatterns=[
    path('create/',create_schedule),
    path('<int:schedule_id>/',edit_schedule,name='schedule'),
    path('<int:schedule_id>/delete/',delete_schedule,name='schedule_delete'),
    path('',scheduleList.as_view(),name='schedule_list'), #lists schedules for a user
]
