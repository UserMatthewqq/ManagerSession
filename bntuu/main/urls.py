from django.urls import path
from . import views
from .views import MyAction, create_room, enter_room, room_detail

urlpatterns = [
    path('', views.index),
    path('git', views.git, name='git'),
    path('video', views.video),
    path('board', views.board, name='board'),
    path('gpt', views.gpt),
    path('messenger', views.messenger),
    path('after_reg', views.after_reg),
    path('myaction/', MyAction.as_view(), name='my-action'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_room/', create_room, name='create_room'),
    path('enter_room/', enter_room, name='enter_room'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),
]
