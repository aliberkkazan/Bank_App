from django.urls import path
from customer_account.api import views as api_views
# Endpoints for APIviews
urlpatterns=[
    path('customers/',api_views.customerListCreateAPIView.as_view(), name= 'customers list'),
    path('accounts/',api_views.accountListCreateAPIView.as_view(), name= 'accounts list'),
    path('customers/<uuid:pk>',api_views.customerDetailAPIView.as_view(), name='customers detail'),
    path('accounts/<uuid:pk>',api_views.accountDetailAPIView.as_view(), name='accounts detail'),
]