from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:shortened_part>', views.redirect_url_view, name="redirect")
]
