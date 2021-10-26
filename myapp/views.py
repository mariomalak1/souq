from django.shortcuts import render
from django.shortcuts import render ,get_object_or_404 ,redirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.http import HttpResponse,Http404

# Create your views here.
@login_required
def home(request):
    items = Product.objects.all()
    return render(request,'home.html',{'items':items})
    
    

@login_required
def choose_pro(request,product_id):
    items = get_object_or_404(Product,pk=product_id)
    pro = Order.objects.all()
    if request.method == 'POST':
        num_meter = request.POST['number_meters']
        user = request.user
        order = Order.objects.create(
            num_meters = num_meter,
            created_by = user,
            product_id = items.pk,
            contact = request.POST['number_phone'],
            )
        return redirect('order_done')
    return render(request, 'choose_pro.html',{'items':items ,'pro':pro})





@login_required
def order_done(request):
    return render(request, 'order_done.html')




#@user_passes_test(lambda u:
#u.is_superuser)
@staff_member_required
def order_admin(request):
    items = Product.objects.all()
    pro = Order.objects.all()
    return render(request, 'orders.html',{'items':items ,'pro':pro})


@login_required
def about(request):
    return render(request, 'about.html')