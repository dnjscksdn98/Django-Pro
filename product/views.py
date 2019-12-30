from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from rest_framework import generics, mixins

from .models import Product
from .forms import RegisterForm
from .serializers import ProductSerializer
from order.forms import OrderForm
from fcuser.decorator import admin_required


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):  # 모든 상품 리스트 보기 API
    serializer_class = ProductSerializer  # 데이터에 대한 검증을 위해서 serializer 등록

    def get_queryset(self):  # 어떤 데이터를 가져올것인지 알기 위해 get_queryset() 오버라이딩
        return Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):  # 상품 상세보기 API
    serializer_class = ProductSerializer

    def get_queryset(self):  # 먼저 모든 데이터를 가져온 이후에 원하는 특정 데이터는 get() 함수에서 가져옴
        return Product.objects.all().order_by("id")

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductList(ListView):
    model = Product
    template_name = "product.html"
    context_object_name = "product_list"


@method_decorator(admin_required, name="dispatch")  # decorator 적용
class ProductCreate(FormView):
    template_name = "register_product.html"
    form_class = RegisterForm
    success_url = "/product/"

    def form_valid(self, form):
        product = Product(
            name=form.data.get("name"),
            price=form.data.get("price"),
            description=form.data.get("description"),
            stock=form.data.get("stock")
        )
        product.save()

        return super().form_valid(form)


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
