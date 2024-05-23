from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_page, name='login_page'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('register/', views.register_page, name='register_page'),
    path('remove_user/', views.remove_user, name='remove_user'),  # Add this line
    path('account/', views.account_view, name='account'),
    path('settings/', views.settings_page, name='settings_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('transaction/', views.transaction_page, name='transaction_page'),
    path('analysis/', views.analysis_page, name='analysis_page'),
    path('analysis/chart/', views.expenses_data, name='expenses_data'),
    path('add_income/', views.add_income, name='add_income'),
]
