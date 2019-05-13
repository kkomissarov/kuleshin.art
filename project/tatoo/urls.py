from django.urls import path
from .views import MainPageView, Login, Logout, DeletePost, CreatePost, UpdatePost


urlpatterns = [
    path('', MainPageView.as_view(), name='main_view'),
    path('login/', Login.as_view(), name='login_view'),
    path('logout/', Logout.as_view(), name='logout_view'),
    path('delete/', DeletePost.as_view(), name='delete_post_view'),
    path('create/', CreatePost.as_view(), name='create_post_view'),
    path('update/', UpdatePost.as_view(), name='update_post_view'),
]


