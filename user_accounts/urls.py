from user_accounts.views import signup,login_user, verify_otp #, dashboard

from django.urls import path

urlpatterns = [
    path('signup/', signup, name= 'signup'),
    path('signin/', login_user, name= 'signin'),
    #path('dashboard/', dashboard, name='dashboard'),
    path('otp/',verify_otp,name='otp')
]