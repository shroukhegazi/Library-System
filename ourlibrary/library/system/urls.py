from django.urls import path
from system.views import home, about, allbooks, myboard, setting, book, loginuser, register, Logoutueser,process,borrowed,return_Book,std_delete

urlpatterns = [
    path('system/loginuser/', loginuser, name="loginuser"),
    path('system/register/', register, name="register"),
    path('system/Logout', Logoutueser, name="Logoutueser"),
    path('system/home/', home, name="libhome"),
    path('system/about/', about, name="aboutUs"),
    path('system/allbooks/', allbooks, name="allbooks"),
    path('system/book/<int:id>', book, name="book"),
    path('system/myboard/', myboard, name="myboard"),
    path('system/setting/', setting, name="setting"),
    path('system/std_delete/', std_delete, name="std_delete"),
    path('system/borrowed/', borrowed, name="borrowed"),
    path('system/br_process/<int:id>', process, name="br_process"),
    path('system/return/<int:id>', return_Book, name="return"),
]
