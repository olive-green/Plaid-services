from django.contrib import admin
from django.urls import path
from plaid_integration_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-user/', views.RegisterUser.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('token-exchange/', views.TokenExchange.as_view(), name="token-exchange"),
    path('get-transactions/', views.GetTransactions.as_view(), name="transactions"),
    path('get-accounts/', views.GetAccounts.as_view(), name="account"),
    path('update-transaction/', views.TransactionUpdate.as_view(), name="update-transaction-hook"),
]
