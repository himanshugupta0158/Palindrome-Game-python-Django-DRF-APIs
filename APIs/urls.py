from django.urls import path
from .views import UserCreateView, UserView, UserDeleteView, getBoardView, ListGamesView, UserLogin, UserLogout, UpdateBoardView, CombinedUpdateBoardView


urlpatterns = [
    # User APIs
    path('create-user/', UserCreateView.as_view(), name='create_user'),
    path('user-view/', UserView.as_view(), name='user_view'),
    # path('update-user/<int:user_id>/', UserUpdateView.as_view(), name='update_user'),
    # path('delete-user/<int:user_id>/', UserDeleteView.as_view(), name='delete_user'),
    # Define URLs for update_user and delete_user using UserView

    # User Login
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),


    # Game APIs
    path('getBoard/', getBoardView.as_view(), name='getBoard'),
    path('updateBoard/', UpdateBoardView.as_view(), name='updateBoard'),
    path('combined-updateBoard/', CombinedUpdateBoardView.as_view(), name='combined-updateBoard'),
    path('list-games/', ListGamesView.as_view(), name='list_games'),
]
