from django.urls import path
from .views import home, RegisterView, LoginView

from django.contrib.auth import views as auth_views
from .views import LoginView, ProfileView
from .forms import LoginForm

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),

    path('login/', LoginView.as_view(redirect_authenticated_user=True,
                                     template_name='users_templates/login.html',
                                     authentication_form=LoginForm),
         name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users_templates/logout.html'),
         name='logout'),

    path('profile/', ProfileView.as_view(), name='profile'),
]
