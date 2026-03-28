# api/urls.py
from django.urls import path
from . import views  # ← Important

urlpatterns = [
    # Tes routes existantes
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/profile/', views.profile, name='profile'),
    path('auth/profile/delete/', views.delete_account, name='delete_account'),
    
    # Routes pour ViewSets (si tu utilises un router)
    # ...
    
    # 👇 AJOUTE CETTE LIGNE ICI :
    path('test/', views.test_api, name='test-api'),
]