from django.shortcuts import render, redirect
from .forms import HallForm
from .models import Hall

# Create your views here.


def hall_l(request):
    context = {'hall_l': Hall.objects.all()}
    return render(request, "hall/hall_l.html", context)


def hall_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = HallForm()
        else:
            hall = Hall.objects.get(pk=id)
            form = HallForm(instance=hall)
        return render(request, "hall/hall_f.html", {'form': form})
    else:
        if id == 0:
            form = HallForm(request.POST)
        else:
            hall = Hall.objects.get(pk=id)
            form = HallForm(request.POST,instance= hall)
        if form.is_valid():
            form.save()
        return redirect('/list')


def hall_delete(request,id):
    hall = Hall.objects.get(pk=id)
    hall.delete()
    return redirect('/list')
