from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view as doc_schema_view
from drf_yasg import openapi

schema_view = doc_schema_view(
    openapi.Info(
        title='Online Shop',
        default_version='v1',
        description='Online shopping',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='olimovotkirbek49@gmail.com'),
        license=openapi.License(name='Alimov Brand'),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('api/v1/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),
    path('accounts/',include('allauth.urls')),
    path('openapi/', get_schema_view( # new
        title="Blog API",
        description="A sample API for learning DRF",
        version="1.0.0"
    ), name='openapi-schema'),
    path('swagger/',schema_view.with_ui(
        'swagger',cache_timeout=0),name = 'schema_swagger_ui'),
    path('redoc/',schema_view.with_ui(
        'redoc',cache_timeout=0),name='schema_redoc'),
    path('',include('shop.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
