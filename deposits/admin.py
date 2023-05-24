from django.contrib import admin
from deposits.models import Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass
