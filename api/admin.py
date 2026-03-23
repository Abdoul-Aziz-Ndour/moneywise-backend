from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Categorie, Transaction, AlerteBudget


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active', 'date_creation')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {'fields': ('date_creation',)}),
    )
    readonly_fields = ('date_creation',)


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'icone', 'utilisateur')
    list_filter = ('type',)
    search_fields = ('nom', 'utilisateur__email')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'categorie', 'montant', 'type', 'date')
    list_filter = ('type', 'date', 'categorie')
    search_fields = ('utilisateur__email', 'description')
    readonly_fields = ('date',)


