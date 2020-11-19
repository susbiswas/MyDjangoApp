from django.urls import path

from .views import detail,room,add_meetings

urlpatterns = [
    path('<int:id>',detail , name ="detail"),
    path('rooms',room, name = "rooms"),
    path('addmeeting',add_meetings, name = "addmeeting")
]