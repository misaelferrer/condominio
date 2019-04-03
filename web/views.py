from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse

# Create your views here.
def index(request):
	obj = Menu.objects.all()
	return render(request, 'base/base_web.html',{'links':obj})