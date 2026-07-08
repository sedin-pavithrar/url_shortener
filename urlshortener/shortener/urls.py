from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.home_view, name="home"),
    path("<str:short_code>/", views.redirect_url, name="redirect_url"),
    path("update/<int:id>/", views.update_url, name="update_url"),
    path("delete/<int:id>/", views.delete_url, name="delete_url"),
]
