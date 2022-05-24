from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login_out/', views.login_out, name='login_out'),
    path('login_handle/', views.login_handle, name='login_handle'),

]
