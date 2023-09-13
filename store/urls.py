from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('view_item/<str:pk>', views.ItemView, name="view_item"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
 	path('login/', views.LoginUser, name="login"),
  	path('logout/', views.LogoutUser, name="logout"),
    path('register/', views.registerUser, name="register")

]