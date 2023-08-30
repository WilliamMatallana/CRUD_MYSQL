from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='company_list'),
    path('companies/<int:id>', CompanyView.as_view()),
    path('companies/put/', CompanyView.as_view()),
    path('companies/delete/', CompanyView.as_view()),


]