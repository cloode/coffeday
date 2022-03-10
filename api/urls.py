from django.urls import path

from api.api_views import CategoryListAPIView, ProductAPIView, ProductDetailAPIView, CommentCreateAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name="api_categories"),
    path('products/', ProductAPIView.as_view(), name="api_products"),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),
    path('comment/', CommentCreateAPIView.as_view())
]