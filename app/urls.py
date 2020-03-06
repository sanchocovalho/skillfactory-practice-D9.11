from app import views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    # path('categories/', views.CategoryView.as_view(), name='category-list'),
    # path('categories/<int:pk>', views.CategoryView.as_view(), name='category-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
]
