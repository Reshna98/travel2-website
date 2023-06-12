from . import views
from django.urls import path

urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('budget',views.budget,name='budget'),
     path('india',views.india,name='india'),
       path('book',views.book,name='book'),
   ]