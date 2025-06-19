from django.shortcuts import render, redirect
from app.models import Profesor
from app.forms import ProfesorForm

# Create your views here.
def inicio(request):
    return render(request,'inicio.html',{})

def menu(request):
    return render(request,'menu.html',{})

## ********************************  ##
##     Manejo de Profesores          ##
## ********************************  ##
def profesorNew(request):
    form = ProfesorForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('/showprofesor')
        except:
            pass
    else:
        form = ProfesorForm
    return render(request,'profesorNew.html',{'form':form})

def profesorShow(request):
    profesor = Profesor.objects.all()
    return render(request,'profesorShow.html',{'profesor':profesor})

def profesorEdit(request, idprofesor):
    profesor = Profesor.objects.get(idprofesor=idprofesor)
    return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorUpdate(request,idprofesor):
    profesor = Profesor.objects.get(idprofesor=idprofesor)
    form = ProfesorForm(request.POST,instance=profesor)
    if form.is_valid():
        form.save()
        return redirect("/showprofesor")
    return render(request,'profesorEdit.html',{'profesor':profesor})

def profesorDestroy(request,idprofesor):
    profesor=Profesor.objects.get(idprofesor=idprofesor)
    profesor.delete()
    return redirect("/showprofesor")

## ********************************  ##
##   FIN Manejo de Profesores        ##
## ********************************  ##
