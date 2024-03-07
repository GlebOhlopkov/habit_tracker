from django.urls import path

from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDeleteAPIView

app_name = 'users'

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
]
