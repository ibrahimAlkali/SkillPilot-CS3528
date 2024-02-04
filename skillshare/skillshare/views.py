from django.shortcuts import render
from django.http import HttpResponse

# View for hello.html
def say_hello(request):
    return render(request, 'hello.html')

# View for IForm.html
def iform(request):
    return render(request, 'IForm.html')

# View for SForm.html
def sform(request):
    return render(request, 'SForm.html')

