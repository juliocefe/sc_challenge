from django.db import models
import uuid


class Account(models.Model):
    name = models.CharField(max_length=30)
    extra_id = models.UUIDField(default=uuid.uuid4, editable=False)
    transactions_file = models.FileField(upload_to="transactions_files/")


# TODO remove plural name to this class
class Transactions(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    oncredit = models.BooleanField(default=False)
    created_at = models.DateTimeField()