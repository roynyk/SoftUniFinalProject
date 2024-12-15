from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume
from .forms import PerfumeForm
from Payment.models import Payment
from django.contrib.auth.decorators import login_required
from perfume_list.models import Perfume
from django.db import transaction


def perfume_list(request):
    perfumes = Perfume.objects.all()
    context = {'perfumes': perfumes}
    return render(request, 'perfume/perfume_list.html', context)

@login_required
def add_perfume(request):
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('perfume_list')
    else:  # Tangani GET request
        form = PerfumeForm()

    context = {'form': form}
    return render(request, 'perfume/add_perfume.html', context)

@login_required
def edit_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save() 
            return redirect('perfume_list')
    else:
        form = PerfumeForm(instance=perfume)

    context = {'form': form, 'perfume': perfume}
    return render(request, 'perfume/edit_perfume.html', context)

@login_required
def delete_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    
    if request.method == 'POST':
        perfume.delete()
        return redirect('perfume_list')
    
    context = {'perfume': perfume}
    return render(request, 'perfume/delete_perfume.html', context)

@login_required
def add_to_payment(request, perfume_id):
    if request.method != "POST":
        # Redirect ke halaman sebelumnya jika request GET
        return redirect(request.META.get('HTTP_REFERER', 'perfume_list'))

    perfume = get_object_or_404(Perfume, id=perfume_id)
    try:
        with transaction.atomic():
            perfume = Perfume.objects.select_for_update().get(id=perfume_id)
            existing_payment = Payment.objects.filter(user=request.user, perfume=perfume).first()

            if not existing_payment:
                Payment.objects.create(
                    user=request.user,
                    perfume=perfume,
                    quantity=1,
                    total_price=perfume.price
                )
            else:
                existing_payment.quantity += 1
                existing_payment.total_price = existing_payment.quantity * perfume.price
                existing_payment.save()

            perfume.stock -= 1
            perfume.is_available = perfume.stock > 0
            perfume.save()
    except Exception as e:
        
        return redirect(request.META.get('HTTP_REFERER', 'perfume_list'))

    return redirect(request.META.get('HTTP_REFERER', 'perfume_list'))


