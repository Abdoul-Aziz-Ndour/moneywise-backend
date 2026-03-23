from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Transaction, Categorie

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'first_name', 'is_staff']
    ordering = ['email']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'type', 'montant', 'categorie', 'date']
    list_filter = ['type', 'date']

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'utilisateur']