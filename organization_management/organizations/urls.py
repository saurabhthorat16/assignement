from django.urls import path
from .views import OrganizationListView, OrganizationDetailView, UserCreateView  # ... other views

urlpatterns = [
    path('organizations/', OrganizationListView.as_view()),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view()),
    path('users/', UserCreateView.as_view()),
    # ... add more URL patterns for other functionalities
]
