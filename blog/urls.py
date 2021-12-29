from django.urls import path
from .views import BlogDetailView, BlogListView , BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post-edit'),
    path('post/new/', BlogCreateView.as_view(), name='post-new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail')
]
