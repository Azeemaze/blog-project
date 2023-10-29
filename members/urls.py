from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangeView, ProfilePageView,EditProfilePageView,CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='app/change-password.html'))
    path('password/',PasswordChangeView.as_view()),
    path('password_success/',views.password_success, name='password_success'),
    path('<int:pk>/profile',ProfilePageView.as_view(),name='profile_pageview'),
    path('CreateProfilePage/',CreateProfilePage.as_view(),name='CreateProfilePage')


]