from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('updatadat/<int:stid>', views.updatadat, name='updatadat'),
    path('useradd/', views.useradd, name='useradd'),
    path('deletedata/<int:stid>', views.deletedata, name='deletedata'),
    path('userlogout/',views.userlogout),
    path('searchname/', views.searchname, name="searchname"),
]