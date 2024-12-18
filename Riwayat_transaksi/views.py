from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import TransactionHistory, models
from Payment.models import Payment



@login_required
def complete_order(request):
    if request.method == 'POST':
        # Ambil metode pembayaran dari form
        payment_method = request.POST.get('payment_method')

        if not payment_method:
            return redirect('payment_list')

    payments = Payment.objects.filter(user=request.user)

    if payments.exists():
        try:
            with transaction.atomic():
                for payment in payments:
                    TransactionHistory.objects.create(
                        date=payment.date,
                        user=payment.user,
                        payment_method=payment_method,
                        brand=payment.perfume.brand,
                        perfume=payment.perfume,
                        quantity=payment.quantity,
                        total_price=payment.total_price,
                    )
                    payment.delete()
        except Exception as e:
            return redirect('payment_list')  # Jika terjadi kesalahan, kembali ke daftar pembayaran

    return redirect('transaction_history')  # Alihkan ke halaman riwayat transaksi


@login_required
def transaction_history(request):
    transactions = TransactionHistory.objects.filter(user=request.user).order_by('-id')
    total_price = transactions.aggregate(total_price=models.Sum('total_price'))['total_price'] or 0

    has_transactions = transactions.exists()

    return render(request, 'riwayat_transaksi/transaction_history.html', {
        'transactions': transactions,
        'total_price': total_price,
        'has_transactions': has_transactions,  # Kirim flag ke template
    })

