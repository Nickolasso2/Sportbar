from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/',Register.as_view(), name='register'),
    path('login/',LoggingIn.as_view() , name='login'),
    path('logout/',log_out , name='logout'),
    path('category/<str:slug>/',CategoryDetail.as_view() , name='category'),
    path('category_list/',CategoryList.as_view() , name='categories'),
    path('book_table/',BookTable.as_view() , name='book_table'),
    path('subsribe/',Subscription.as_view() , name='subscribe'),
 
]