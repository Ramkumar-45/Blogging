from django.urls import path
from .views import HomeView, DetailPost, AddPostView, UpdatePostView, DeletePostView, ContactPage

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('post/<int:pk>', DetailPost.as_view(), name='post'),

    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('updatepost/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('deletepost/<int:pk>', DeletePostView.as_view(), name='delete'),

    path('contact/', ContactPage.as_view(), name='contact'),
]
