from django.urls import path,include
from .views import *

app_name = 'myapp'


urlpatterns = [
    path('industry/create/', IndustryTypeCreateView.as_view(), name='industry_create'),
    path('company/create/', CompanyCreateView.as_view(), name='company_create'),
    path('industry/list/', IndustryList.as_view(), name='industry_list'),
    path('company/list/', CompanyList.as_view(), name='company_list'),
]