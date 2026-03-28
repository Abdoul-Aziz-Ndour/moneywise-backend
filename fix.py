f = open('api/urls.py', 'w', encoding='utf-8')
f.write("""from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'categories', views.CategorieViewSet, basename='categorie')

urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/profile/', views.profile, name='profile'),
    path('auth/profile/delete/', views.delete_account, name='delete_account'),
    path('test/', views.test_api, name='test-api'),
]

urlpatterns += router.urls
""")
f.close()
print('SUCCES !')