from django.shortcuts import render, redirect


def home(request):
  return render(request, 'chat/base.html')

def chatPage(request):
    return render(request, "chat/chatPage.html")

def chatRoom(request):
   return render(request, "chat/chatRoom.html")

def messages(request):
   return render(request, "chat/messages.html")

