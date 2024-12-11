from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Perfume
from .forms import PerfumeForm


def perfume_list(request):
    perfumes = Perfume.objects.all()
    if not perfumes.exists():
        messages.info(request, "Belum ada parfum yang tersedia.")
    context = {
        'perfumes': perfumes
    }
    return render(request, 'perfume/perfume_list.html', {'perfumes': perfumes})


def add_perfume(request):
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('perfume_list') 
        else:
            messages.error(request, "Terjadi kesalahan. Periksa kembali data yang dimasukkan.")
    else:
        form = PerfumeForm()
    context = {'form': form}
    return render(request, 'perfume/add_perfume.html', context)

def edit_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save() 
            return redirect('perfume_list')
        else:
            messages.error(request, "Terjadi kesalahan. Periksa kembali data yang dimasukkan.")
    else:
        form = PerfumeForm(instance=perfume)

    context = {'form': form, 'perfume': perfume}
    return render(request, 'perfume/edit_perfume.html', context)

def delete_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    if request.method == 'POST':
        perfume.delete()
        return redirect('perfume_list')
    context = {'perfume': perfume}
    return render(request, 'perfume/delete_perfume.html', context)
