"""ecommerce URL Configuration
"""


from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from .product.views import CategoryView, BrandView, ProductView


router = DefaultRouter()
router.register(r"category",CategoryView)
router.register(r"brand", BrandView)
router.register(r"product", ProductView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]

