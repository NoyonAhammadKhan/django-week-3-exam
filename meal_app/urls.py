from django.urls import path, include
from . import views
urlpatterns = [
    path('show_items/', views.show_item, name="show_items"),
]
