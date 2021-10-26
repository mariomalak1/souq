from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_viwes
urlpatterns = [
    path('signup/',views.signup ,name='signup'),
    path('logout/',auth_viwes.LogoutView.as_view(),name='logout'),
    path('login/',auth_viwes.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/change_password/',auth_viwes.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change'),
    path('settings/change_password/done/',auth_viwes.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),
    path('account/',views.UserUpdateView.as_view(),name='my_account')

]