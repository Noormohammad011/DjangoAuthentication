
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),

]
