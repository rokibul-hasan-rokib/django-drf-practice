from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.decorators import role_required
from ecommerce.models import Product, Order, Vendor


# -------------------------
# SUPER ADMIN DASHBOARD
# -------------------------
@login_required
@role_required(allowed_roles=["admin"])
def superadmin_dashboard(request):
    total_vendors = Vendor.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_sales = sum(order.total_amount for order in Order.objects.all())
    context = {
        "total_vendors": total_vendors,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_sales": total_sales,
    }
    return render(request, "dashboard/superadmin_dashboard.html", context)


# -------------------------
# VENDOR DASHBOARD
# -------------------------
@login_required
@role_required(allowed_roles=["vendor"])
def vendor_dashboard(request):
    vendor = request.user.vendor_profile  # OneToOne relation
    products = vendor.products.all()
    orders = Order.objects.filter(items__vendor=vendor).distinct()
    total_sales = sum(item.price * item.quantity for item in vendor.products.values_list("orderitem__price", "orderitem__quantity"))

    context = {
        "vendor": vendor,
        "products": products,
        "orders": orders,
        "total_sales": total_sales,
    }
    return render(request, "dashboard/vendor_dashboard.html", context)
