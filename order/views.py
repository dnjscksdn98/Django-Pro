from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from fcuser.decorator import login_required
from .forms import OrderForm
from .models import Order


@method_decorator(login_required, name="dispatch")  # decorator 적용
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = "/product/"

    def form_invalid(self, form):  # 주문에 실패를 했을때
        return redirect("/product/" + str(form.product))  # 다시 상품의 상세보기 페이지로 이동

    # 3. Form을 생성할때 어떤 인자값을 전달해줄것인지 정하는 함수
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({"request": self.request})
        return kw


@method_decorator(login_required, name="dispatch")  # decorator 적용
class OrderList(ListView):
    template_name = "order.html"
    context_object_name = "order_list"

    def get_queryset(self, **kwargs):  # 보여줄 queryset을 지정하는 함수(queryset overriding)
        queryset = Order.objects.filter(
            fcuser__email=self.request.session.get("user")  # 현재 사용자의 주문정보만 조회
        )
        return queryset
