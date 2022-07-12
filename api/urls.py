from django.urls import include, path
# from .views import ProductList,ProductDetail,ProductAdd
from rest_framework import routers

from api.views import ProductViewSet, UserViewSet

router = routers.SimpleRouter()
router.register('products',ProductViewSet)
router.register('users',UserViewSet)

urlpatterns = [
    path('',include(router.urls))
    
#     path('products/',ProductList.as_view()),
#     path('products/<int:pk>/',ProductDetail.as_view()),
#     path('addproduct/',ProductAdd.as_view())
 ]