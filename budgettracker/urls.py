from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup, name='signup'),
    path("login", views.login_view, name="login"),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('about_us', views.about_us, name='about_us'),
    path('add_expense', views.add_expense, name='add_expense')
]
