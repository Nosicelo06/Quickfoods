from django.shortcuts import render
from .models import Food

def home(request):
   foods= Food.objects.filter(available=True)
   return render(request, 'myapp/index.html', {'foods': foods})