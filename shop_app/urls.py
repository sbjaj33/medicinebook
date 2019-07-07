from django.urls import path
from django.conf.urls import url
from shop_app import views
app_name="shop_app"

urlpatterns=[
    path('',views.Index.as_view(),name='index'),
    path('register/',views.Register,name="register"),
    path('login/',views.User_login,name="userLogin"),
    path('logout/',views.user_logout,name="userLogout"),
    path('Aboutus/',views.Aboutus.as_view(),name="aboutus"),
    path('stock/list/',views.Stocklist.as_view(),name="StockList"),
    url(r'(?P<pk>\d+)/',views.Stockdetail.as_view(),name="StockDetail"),
    path('stock/new/',views.Createstock.as_view(),name="StockCreate"),
    path(r'update/(?P<pk>\d+)/',views.StockUpdateView.as_view(),name="update"),
    path(r'delete/(?P<pk>\d+)/',views.StockDeleteView.as_view(),name="delete"),
    path('search/',views.SearchResultView.as_view(),name="SearchData"),

]
