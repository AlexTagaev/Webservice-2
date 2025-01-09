from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start(request):
    return render(request, 'chatbot/start.html')

def chatbot(request):
    return render(request, 'chatbot/chatbot.html')

def test(request):
    return HttpResponse('Тестовая страница')