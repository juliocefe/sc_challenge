from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=30)
    transactions_file = models.FileField(upload_to="transactions_files/")

# TODO remove plural name to this class
class Transactions(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    created_at = models.DateTimeField()