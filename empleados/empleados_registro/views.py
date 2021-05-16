from django.shortcuts import render, redirect
from .forms import EmpleadosForm
from .models import Empleados

# Create your views here.


def empleados_list(request):
    context = {'empleados_lista': Empleados.objects.all}
    return render(request, "empleados_registro/empleados_list.html", context)

# def empleados_form(request):
   # if request.method == "GET":

   #     form = EmpleadosForm()

    #    return render(request, "empleados_registro/empleados_form.html", {'form': form})
   # else:

    #    form = EmpleadosForm(request.POST)
    #  if form.is_valid():
    #    form.save()
    # return redirect('/empleados/lista')

# def empleados_form(request, id=0):
 #   if request.method == "GET":
 #       if id == 0:
 #           form = EmpleadosForm()
 #       else:
#            empleados = Empleados.objects.get(pk=id)
  #          form = EmpleadosForm(instance=empleados)
  #      return render(request, "empleados_registro/empleados_form.html", {'form': form})
#    else:

 #       form = EmpleadosForm(request.POST)

   #     if form.is_valid():
  #          form.save()
  #      return redirect('/empleados/lista')


def empleados_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmpleadosForm()
        else:
            empleados = Empleados.objects.get(pk=id)
            form = EmpleadosForm(instance=empleados)
        return render(request, "empleados_registro/empleados_form.html", {'form': form})
    else:
        if id == 0:
            form = EmpleadosForm(request.POST)
        else:
            empleados = Empleados.objects.get(pk=id)
            form = EmpleadosForm(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
        return redirect('/empleados/lista')


# def empleados_form(request):
  #  form = EmpleadosForm()
  #  return render(request, "empleados_registro/empleados_form.html", {'form': form})


def empleados_delete(request, id):
    empleados = Empleados.objects.get(pk=id)
    empleados.delete()
    return redirect('/empleados/lista')
