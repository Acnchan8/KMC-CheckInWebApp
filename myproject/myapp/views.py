from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, 'myapp/index.html')

# def some_function(request):
#     # Perform backend logic here
#     context = {'data': 'Hello, world!'}
#     return render(request, 'myapp/some_template.html', context)


def login_view(request):
    return render(request, 'myapp/login.html')

def database_view(request):
    return render(request, 'myapp/database.html')