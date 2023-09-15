from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Lobby,name = 'lobby'),
    path("room/",views.Room,name = 'room'),
    path("get_token/",views.getToken,name = 'token'),
    path('create_member/',views.createMember,name = 'member'),
    path('get_member/',views.getMember,name = 'getmember'),
    path('delete_member/',views.deleteMember,name = 'deletemember')
]