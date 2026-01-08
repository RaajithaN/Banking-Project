from user_accounts.views import signup, signin #, dashboard

from django.urls import path

urlpatterns = [
    path('signup/', signup, name= 'signup'),
    path('signin/', signin, name= 'signin'),
    #path('dashboard/', dashboard, name='dashboard'),
]