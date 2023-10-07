from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars, name='cars'),
    path('contact/', views.contact, name='contact'),
    path('car/<str:pk>', views.car, name='car'),
    path('book-car/<str:pk>', views.book_car, name='book-car'),
    path('book-details/<str:pk>', views.book_details, name='book-details'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('cancel-booking/<str:pk>', views.cancel_booking, name='cancel-booking'),
    path('booking-confirmation/<str:pk>', views.book_confirmation, name='booking-confirmation'),
    path('booking-list/', views.booking_list, name='booking-list')
]
