from django.urls import path

from accounts.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(), name='login_url'),
    path('register/', RegisterView.as_view(), name='register_url')
]
