from django.urls import path,include
from . import views

urlpatterns=[
    path('login/', views.login_view,name='login'),
    path('<int:user_id>/', views.account_view,name='profile'),
    path('register/', views.register_view,name='register'),
    path('<int:user_id>/logout/', views.logout_view),
    path ('<int:user_id>/edit/change_password/',views.change_password_view),\
    path('<int:user_id>/edit/', views.account_edit_view),
    path('<int:user_id>/edit/delete/', views.account_delete_view),

    #for schedules stuff
    path('<int:user_id>/schedules/',include('schedules.urls')),
]
