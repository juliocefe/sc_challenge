from django.contrib import admin
from .models import Account, Transactions

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    pass

