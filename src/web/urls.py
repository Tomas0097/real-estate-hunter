from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("parse-marketplace/<str:marketplace_code>/", views.parse_marketplace, name="parse-marketplace")
]
