from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def fun_index(request):
    obj_place=Place.objects.all()
    obj_team=Team.objects.all()
    return render(request,"index.html",{'result':obj_place,'result_team':obj_team})