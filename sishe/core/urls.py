from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('index/', views.Index, name="index")
]
