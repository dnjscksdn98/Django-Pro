from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import OrderForm
from fcuser.decorator import admin_required


class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"


@method_decorator(admin_required, name="dispatch")  # decorator 적용
class ProductCreate(FormView):
    template_name = "register_product.html"
    form_class = RegisterForm
    success_url = "/product/"


class ProductDetail(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"

    # 별도로 원하는 데이터를 가져오는 함수(페이지 상세보기에서 OrderForm을 가져오기)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 2. OrderForm 객체 생성시 request 전달, OrderForm 안에서 request에 접근하기 위해서
        context["form"] = OrderForm(self.request)
        return context
