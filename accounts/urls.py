from django.urls import path,include
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edite_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('accounts/profile/', views.ShowProfileView.as_view(), name='show_profile'),
]