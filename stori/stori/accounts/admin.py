from django.contrib import admin
from .models import Account, Transactions


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def save_model(self, request, obj: Account, form, change) -> None:
        # name the field with our uiid value
        print("creating file from django")
        obj.transactions_file.name = str(obj.extra_id) + ".csv"
        return super().save_model(request, obj, form, change)


@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    pass

