from django.urls import path
from .views import Snacklistview , SnackDetailview

urlpatterns = [
    path('',Snacklistview.as_view(),name='snacks'),
    path("<int:pk>/", SnackDetailview.as_view(),name="snacks_detail"),
]