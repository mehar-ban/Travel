from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
#def demo(request):
 #  return render(request,"home.html")
#def about(request):
#   return render(request,"about.html")
#def contact(request):
#   return HttpResponse("hello am contact")

#passing value(using DICTIONARY)
#def demo(request):
 #  name="India"
 #  return render(request,"home.html",{'obj':name})
#def add(request):
#   x=int(request.GET['num1'])
#   y=int(request.GET['num2'])
#   res=x+y
#   return render(request,"about.html",{'result':res})

def demo(request):
   place = Place.objects.all()
   team = Team.objects.all()
   return render(request,"index.html",{'result':place,'res':team})
