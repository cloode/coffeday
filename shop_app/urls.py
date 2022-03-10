from django.urls import path
from shop_app.views import ProductList, ProductDetail, AddComment, AddDislikeComment, \
    AddLikeComment, CommentDelete, ProfileView, ProfileEditView, CategoryProductView, ProductFilterView

app_name = 'shop'

urlpatterns = [
    path('', ProductList.as_view(), name="product_list"),
    path('products/', ProductFilterView.as_view(), name="product_filter"),
    path('category/<slug:category_slug>/', CategoryProductView.as_view(), name="category_product"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile_view"),
    path('profile/<int:pk>/update/', ProfileEditView.as_view(), name="profile_edit"),
    path('<int:product_pk>/comment/<int:pk>/like/', AddLikeComment.as_view(), name="comment_like"),
    path('<int:product_pk>/comment/<int:pk>/dislike/', AddDislikeComment.as_view(), name="comment_dislike"),
    path('<slug:product_slug>/comment/delete/<int:pk>/', CommentDelete.as_view(), name="comment_delete"),
    path('comment/<int:pk>/', AddComment.as_view(), name="add_comment"),
    path('<slug:slug>/', ProductDetail.as_view(), name="product_detail"),
]

