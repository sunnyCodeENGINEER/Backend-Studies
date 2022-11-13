from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 1
    y = 3
    return x

def sayHello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', {'name': 'Emma'})