from django.db import models
import uuid

class Post(models.Model):
    """
    A model representing a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Payment(models.Model):
    """
    A model representing a payment record.
    """
    id = models.CharField(
        max_length=36,
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )  # Use a UUID for the custom ID
    name = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS,
        default='Unpaid'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status} - ${self.total}"
    
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    gateway = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(default='0000-00-00 00:00:00')  # Note: This default value is non-standard.
    account_number = models.CharField(max_length=100, null=True, blank=True)
    sub_account = models.CharField(max_length=250, null=True, blank=True)
    amount_in = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    amount_out = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    accumulated = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    code = models.CharField(max_length=250, null=True, blank=True)
    transaction_content = models.TextField(null=True, blank=True)
    reference_number = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_transactions'
        managed = True
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f"Transaction {self.id} - {self.gateway}"
