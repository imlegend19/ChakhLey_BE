"""ChakhLey_BE URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

admin.site.site_header = "Chakh Ley Administration"
admin.site.site_title = "Chakh Ley Administration"
admin.site.index_title = 'Admin'

schema_view = get_schema_view(
    openapi.Info(
        title="Chakh Ley API",
        default_version='v1',
        description="API based on DRF YASG for Chakh Ley",
        contact=openapi.Contact(email="support@chakhley.co.in"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex', 'ssv'],
    public=False,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('api/user/', include('drf_user.urls')),
    path('api/location/', include('location.urls', namespace='location')),
    path('api/order/', include('order.urls', namespace='order')),
    path('api/restaurant/', include('restaurant.urls', namespace='restaurant')),
    path('api/product/', include('product.urls', namespace='product')),
    path('api/business/', include('business.urls', namespace='business')),
    path('api/employee/', include('employee.urls', namespace='employee')),
    path('api/user_rating/', include('user_rating.urls', namespace='user rating')),
    path('api/transactions/', include('transactions.urls', namespace='transactions')),
    path('', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
