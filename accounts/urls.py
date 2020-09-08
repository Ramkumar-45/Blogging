from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, CreateProfileView, EditProfilePage, UserEditView, ProfilePage, PasswordChangeView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),

    path('createprofile/', CreateProfileView.as_view(), name='createprofile'),
    path('<int:pk>/editprofile/', EditProfilePage.as_view(), name='editprofile'),
    path('edit_profile/', UserEditView.as_view(), name='profile'),
    path('<int:pk>/profile/', ProfilePage.as_view(), name='profiledetail'),

    path('password/', PasswordChangeView.as_view(), name='passwordchange'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name='registration/passwordreset.html'),
         name='password'),
    path('passwordresetsent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html')),
    path('passwordreset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html.html')),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html')),
]
