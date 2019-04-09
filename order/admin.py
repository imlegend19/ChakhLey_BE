from django.contrib import admin

from drfaddons.admin import CreateUpdateAdmin

from .models import Order


class DeliveryInLine(admin.TabularInline):
    from .models import Delivery

    model = Delivery
    extra = 0
    exclude = ('created_by', )


class SubOrderInLine(admin.TabularInline):
    from .models import SubOrder

    model = SubOrder
    extra = 0
    exclude = ('created_by', )


class OrderAdmin(CreateUpdateAdmin):
    list_display = ('id', 'restaurant', 'name', 'mobile', 'status', 'total')
    list_filter = ('status', 'restaurant', )
    readonly_fields = ('total', )
    inlines = (SubOrderInLine, DeliveryInLine)

    def get_changeform_initial_data(self, request):
        from restaurant.models import Restaurant

        data = {}
        if 'restaurant__id' in request.GET:
            restaurant = Restaurant.objects.get(pk=request.GET['restaurant__id'])
            data['restaurant'] = restaurant

        return data


admin.site.register(Order, OrderAdmin)
