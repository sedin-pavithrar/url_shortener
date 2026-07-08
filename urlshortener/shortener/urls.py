from django.urls import path
from .import views 

urlpatterns = [
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("",views.home_view,name = "home"),
    path("<str:short_code>/", views.redirect_url, name="redirect_url"),

]

