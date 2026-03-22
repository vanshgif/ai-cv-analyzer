from django.urls import path
from .views import upload_cv

urlpatterns = [
    path('upload-cv/', upload_cv),
]