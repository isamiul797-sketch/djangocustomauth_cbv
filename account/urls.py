from django.urls import path
from account.views import HomeView,LoginView,RegistrtionView,PasswordResetConfirmView,CustomPasswordResetView,activate_account
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/',LoginView.as_view(), name='login'),
    path('register/',RegistrtionView.as_view(), name='register'),
    path('activate/<str:uidb64>/<str:token>/',activate_account, name='activate'),
    path('password_reset/',CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('logout/',LogoutView.as_view(),name='logout'),

]