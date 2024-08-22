from   djangoproject.accounts. views import  OrderApproveView
from django.urls import path,include

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'approve',OrderApproveView)

url_patterns=[
    
]
