from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin

class PostList(LoginRequiredMixin, generics.ListCreateAPIView):
    login_url = '/admin/'
    redirect_field_name = 'login'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(LoginRequiredMixin, generics.RetrieveAPIView):
    login_url = '/admin/'
    redirect_field_name = 'login'
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(LoginRequiredMixin, generics.ListCreateAPIView):
    login_url = '/admin/'
    redirect_field_name = 'login'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(LoginRequiredMixin, generics.RetrieveAPIView):
    login_url = '/admin/'
    redirect_field_name = 'login'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
