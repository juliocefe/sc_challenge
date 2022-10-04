from django.contrib import admin
from .models import Account, Transactions


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    pass

