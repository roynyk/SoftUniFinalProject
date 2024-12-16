from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import PaymentForm  

@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)

    if not payments.exists():
        return render(request, 'payment/payment_list.html', {'payments': None, 'total_payment': 0})

    total_payment = sum(payment.total_price for payment in payments)
    return render(request, 'payment/payment_list.html', {'payments': payments, 'total_payment': total_payment})

@login_required
def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)

    try:
        with transaction.atomic():
    
            perfume = payment.perfume
            perfume.stock += payment.quantity
            perfume.is_available = True
            perfume.save()

            payment.delete()

    except Exception as e:
        pass

    return redirect('payment_list')

@login_required
def decrease_quantity(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)
    
    try:
        with transaction.atomic():
            if payment.quantity > 1:
    
                payment.quantity -= 1
                payment.total_price = payment.quantity * payment.perfume.price
                payment.save()
                
        
                perfume = payment.perfume
                perfume.stock += 1
                perfume.is_available = True
                perfume.save()

    except Exception as e:
        pass
    
    return redirect('payment_list')

@login_required
def payment_order(request):
    if request.method == "POST":
        payment_method = request.POST.get('payment_method')

        payments = Payment.objects.filter(user=request.user)
        for payment in payments:
            payment.payment_method = payment_method
            payment.save()

        return redirect('payment:payment_list') 

    payments = Payment.objects.filter(user=request.user)

    total_price = sum(payment.quantity * payment.perfume.price for payment in payments)

    payment_form = PaymentForm()

    return render(request, 'payment/payment_order.html', {
        'payments': payments,
        'total_price': total_price,
        'payment_form': payment_form,
    })
