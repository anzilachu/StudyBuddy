from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('profie/<str:pk>/',views.userProfile,name='user-profile'),

    path('create_room',views.create,name='create-room'),
    path('update/<str:pk>/',views.update,name='update-room'),
    path('delete/<str:pk>/',views.delete,name='delete-room'),

    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),

    path('update-user/',views.updateUser,name='update-user'),

    path('topics/',views.topicPage,name='topics'),
    path('activity/',views.activityPage,name='activity'),

]
