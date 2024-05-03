from django.urls import path
from django.contrib.auth import views as auth_views
from .views import my_view, signup, login_view, checkout, about_view, contact_view  # Import the login_view function

urlpatterns = [
    path('', my_view, name='home'),  # Define the root URL pattern
    path('my-view/', my_view, name='my-view'),
    path('login/', login_view, name='login'),  # Change to login_view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL remains the same
    path('signup/', signup, name='signup'),
    path('checkout/', checkout, name='checkout'),
    path('about/', about_view, name='about'),  # Add URL pattern for the about page
    path('contact/', contact_view, name='contact'),  # Add URL pattern for the contact page
]
