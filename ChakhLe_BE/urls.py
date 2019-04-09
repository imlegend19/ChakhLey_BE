"""ChakhLe_BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

admin.site.site_header = "Chakh Le Administration"
admin.site.site_title = "Chakh Le Administration"

schema_view = get_schema_view(
    openapi.Info(
        title='Chakh Le API',
        default_version='v1',
        description="API based on DRF YASG for Chakh Le",
        contact=openapi.Contact(email="mahengandhi19@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(AllowAny, )
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui('cache_timeout=None'), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None),
         name='schema-redoc'),
    path('api/user/', include('drf_user.urls')),
    path('api/location/', include('location.urls', namespace='location')),
    path('api/order/', include('order.urls', namespace='order')),
    path('api/restaurant/', include('restaurant.urls', namespace='restaurant')),
    path('api/product/', include('product.urls', namespace='product')),
    path('api/business/', include('business.urls', namespace='business')),
    path('api/employee/', include('employee.urls', namespace='employee')),
    path('api/user_rating/', include('user_rating.urls', namespace='user rating')),
    path('api/transactions/', include('transactions.urls', namespace='transactions')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('jet/', include('jet.urls', 'jet')),
    path('', admin.site.urls),
]
