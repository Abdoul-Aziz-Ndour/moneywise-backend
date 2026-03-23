from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Transaction, Categorie

admin.site.register(User, UserAdmin)
admin.site.register(Transaction)
admin.site.register(Categorie)