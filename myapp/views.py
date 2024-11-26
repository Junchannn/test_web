from django.http import HttpResponse, Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment, Transaction


@staff_member_required
def custom_admin_view(request):
    """
    A custom admin-only view.
    """
    return HttpResponse("This is a custom admin view!")

def create_payment(request):
    """
    Handles the creation of a new payment.
    """
    if request.method == 'POST':
        try:
            name = request.POST['name']
            total = request.POST['total']

            # Validate total
            total = float(total)
            if total <= 0:
                raise ValueError("Total must be greater than zero.")
            # Create a new Payment object
            payment = Payment(name=name, total=total)
            payment.save()

            # Redirect to a detailed view
            return redirect('payment_detail', payment_id=payment.id)

        except (KeyError, ValueError) as e:
            return HttpResponse(f"Error: {str(e)}", status=400)

    return render(request, 'view/post_payment.html')
def payment_detail(request, payment_id):
    """
    Displays payment details.
    """
    payment = get_object_or_404(Payment, id=payment_id)
    
    # Format the 'total' field as VND
    formatted_amount = f"{payment.total:,.0f} ₫".replace(",", ".")
    
    return render(request, 'view/payment.html', {'payment': payment, 'formatted_amount': formatted_amount})


def payment(request):
    """
    Renders the payment page for an example or confirmation.
    """
    return render(request, 'payment.html')

from django.http import JsonResponse

def update_payment(request):
    try:
        # Create and save the transaction
        newtrans = Transaction.objects.create(
            id=request.POST.get('id'),
            gateway=request.POST.get('gateway'),
            transaction_date=request.POST.get('transaction_date'),
            account_number=request.POST.get('account_number'),
            sub_account=request.POST.get('sub_account'),
            amount_in=request.POST.get('amount_in', 0.00),
            amount_out=request.POST.get('amount_out', 0.00),
            accumulated=request.POST.get('accumulated', 0.00),
            code=request.POST.get('code'),
            transaction_content=request.POST.get('transaction_content'),
            reference_number=request.POST.get('reference_number'),
            body=request.POST.get('body'),
            created_at=request.POST.get('created_at')
        )

        # Return detailed transaction data
        return JsonResponse({
            "message": "Transaction created successfully",
            "transaction": {
                "gateway": newtrans.gateway,
                "transaction_date": newtrans.transaction_date,
                "account_number": newtrans.account_number,
                "sub_account": newtrans.sub_account,
                "amount_in": str(newtrans.amount_in),
                "amount_out": str(newtrans.amount_out),
                "accumulated": str(newtrans.accumulated),
                "code": newtrans.code,
                "transaction_content": newtrans.transaction_content,
                "reference_number": newtrans.reference_number,
                "body": newtrans.body,
            }
        }, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

