from django.contrib import admin
from django.urls import path, include
from chat import views as chat_views


#from django.contrib.auth.views import LoginView, LogoutView
 
 
urlpatterns = [
    path("", chat_views.home, name="home"),
    path("chat/", chat_views.chatRoom, name="chat"),
    path('messages/', chat_views.messages, name='message'),
    # path('messages/<int:messages_id>/', chat_views.messages_detail, name='detail')

 
    # login-section
  ]