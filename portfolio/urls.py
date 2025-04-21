from django.urls import path
from portfolio.views import *

app_name = 'portfolio'

urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', resume_view, name='resume'),
    path('services/', services_view, name='services'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('contact/', contact_view, name='contact'),
]