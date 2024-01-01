from django.urls import path
from .views import signup, user_login, user_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
]
