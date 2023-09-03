from django.shortcuts import render, redirect, get_object_or_404
from .models import CrudModel
from .forms import CrudForm


def index(request):
    crud_objects = CrudModel.objects.all()
    return render(request, 'crud_app/index.html', {'crud_objects': crud_objects})


def create(request):
    if request.method == 'POST':
        form = CrudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:index')
    else:
        form = CrudForm()
    return render(request, 'crud_app/create.html', {'form': form})


def update(request, pk):
    crud_object = get_object_or_404(CrudModel, pk=pk)
    if request.method == 'POST':
        form = CrudForm(request.POST, instance=crud_object)
        if form.is_valid():
            form.save()
            return redirect('crud:index')
    else:
        form = CrudForm(instance=crud_object)
    return render(request, 'crud_app/update.html', {'form': form})


def delete(request, pk):
    crud_object = get_object_or_404(CrudModel, pk=pk)
    if request.method == 'POST':
        crud_object.delete()
        return redirect('crud:index')
    return render(request, 'crud_app/delete.html', {'crud_object': crud_object})
